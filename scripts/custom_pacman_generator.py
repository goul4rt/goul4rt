#!/usr/bin/env python3
"""
Script para gerar Pacman contribution graph com temas customizados
Modifica o constants.ts do pacman-contribution-graph para usar os temas customizados
"""

import json
import subprocess
from pathlib import Path
from pacman_theme_generator import get_current_celebration_theme, PACMAN_THEMES


def get_theme_data(theme_name=None):
    """Pega os dados do tema (atual ou específico)"""
    if theme_name:
        if theme_name in PACMAN_THEMES:
            return theme_name, PACMAN_THEMES[theme_name]
        else:
            print(f"⚠️  Tema '{theme_name}' não encontrado, usando padrão")
            return 'default', PACMAN_THEMES['default']
    else:
        return get_current_celebration_theme()


def generate_typescript_theme(theme_name, theme_data):
    """Gera o código TypeScript para o tema"""
    
    # Formata o array de cores
    intensity_colors = ', '.join([f"'{color}'" for color in theme_data['intensityColors']])
    
    theme_code = f"""
	'{theme_name}': {{
		textColor: '{theme_data['textColor']}',
		gridBackground: '{theme_data['gridBackground']}',
		wallColor: '{theme_data['wallColor']}',
		intensityColors: [{intensity_colors}]
	}}"""
    
    return theme_code


def update_types_file(pacman_source_path, theme_name):
    """Atualiza o arquivo types.ts para incluir o novo tema"""
    
    types_file = Path(pacman_source_path) / 'src' / 'types.ts'
    
    if not types_file.exists():
        print(f"⚠️  Arquivo types.ts não encontrado, pulando...")
        return True
    
    content = types_file.read_text(encoding='utf-8')
    
    # Procura pela definição de ThemeKeys (várias possíveis ordens)
    theme_keys_patterns = [
        "export type ThemeKeys = 'github' | 'github-dark' | 'gitlab' | 'gitlab-dark'",
        "export type ThemeKeys = 'github' | 'gitlab' | 'github-dark' | 'gitlab-dark'",
    ]
    
    for old_type in theme_keys_patterns:
        if old_type in content:
            # Adiciona o novo tema ao tipo
            new_type = old_type + f" | '{theme_name}'"
            
            content = content.replace(old_type, new_type)
            types_file.write_text(content, encoding='utf-8')
            print(f"✅ Tipo ThemeKeys atualizado com '{theme_name}'")
            return True
    
    # Verifica se já existe
    if f"'{theme_name}'" in content:
        print(f"ℹ️  Tema '{theme_name}' já existe em types.ts")
        return True
    
    print(f"⚠️  Não foi possível atualizar types.ts automaticamente")
    return True


def update_constants_file(pacman_source_path, theme_name, theme_data):
    """Atualiza o arquivo constants.ts com o novo tema"""
    
    constants_file = Path(pacman_source_path) / 'src' / 'core' / 'constants.ts'
    
    if not constants_file.exists():
        print(f"❌ Arquivo não encontrado: {constants_file}")
        return False
    
    # Lê o arquivo original
    content = constants_file.read_text(encoding='utf-8')
    
    # Verifica se o tema já existe
    if f"'{theme_name}':" in content or f'"{theme_name}":' in content:
        print(f"ℹ️  Tema '{theme_name}' já existe em constants.ts")
        return True
    
    # Gera o código do novo tema
    new_theme_code = generate_typescript_theme(theme_name, theme_data)
    
    # Procura onde inserir o tema (antes do fechamento do objeto GAME_THEMES)
    # Adiciona após o último tema existente
    insert_marker = "'gitlab-dark': {"
    
    if insert_marker in content:
        # Encontra o final do tema gitlab-dark
        gitlab_end = content.find("}", content.find(insert_marker))
        insert_position = content.find("\n", gitlab_end) + 1
        
        # Insere o novo tema
        content = content[:insert_position] + ",\n" + new_theme_code + content[insert_position:]
        
        # Escreve de volta
        constants_file.write_text(content, encoding='utf-8')
        print(f"✅ Tema '{theme_name}' adicionado ao constants.ts")
        return True
    else:
        print("❌ Não foi possível encontrar o marcador para inserir o tema")
        return False


def build_pacman_library(pacman_source_path):
    """Builda a biblioteca do pacman"""
    print("🔨 Buildando biblioteca Pacman...")
    
    try:
        result = subprocess.run(
            ['npm', 'run', 'build'],
            cwd=pacman_source_path,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            print("✅ Build concluído com sucesso!")
            return True
        else:
            print(f"❌ Erro no build:\n{result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout no build")
        return False
    except FileNotFoundError:
        print("❌ npm não encontrado. Certifique-se de que Node.js está instalado")
        return False


def generate_custom_action(pacman_source_path, theme_name):
    """Gera uma versão customizada do index.js da action com o tema"""
    
    action_src = Path(pacman_source_path) / 'github-action' / 'src' / 'index.js'
    
    if not action_src.exists():
        print(f"❌ Arquivo da action não encontrado: {action_src}")
        return False
    
    # Lê o arquivo
    content = action_src.read_text(encoding='utf-8')
    
    # Substitui os temas hardcoded
    content = content.replace(
        'svgContent = await generateSvg(userName, githubToken, "github", playerStyle)',
        f'svgContent = await generateSvg(userName, githubToken, "{theme_name}", playerStyle)'
    )
    
    content = content.replace(
        'svgContent = await generateSvg(userName, githubToken, "github-dark", playerStyle)',
        f'svgContent = await generateSvg(userName, githubToken, "{theme_name}", playerStyle)'
    )
    
    # Escreve de volta
    action_src.write_text(content, encoding='utf-8')
    print(f"✅ Action configurada para usar tema '{theme_name}'")
    return True


def main():
    """Função principal"""
    import sys
    
    print("🎮 Gerador Customizado de Pacman Contribution Graph\n")
    
    # Pega tema atual ou especificado
    theme_name = sys.argv[1] if len(sys.argv) > 1 else None
    celebration, theme_data = get_theme_data(theme_name)
    
    print(f"🎨 Tema selecionado: {celebration}")
    print(f"📝 {theme_data['description']}\n")
    
    # Caminho do source do pacman
    workspace = Path(__file__).parent.parent
    
    # Tenta ambos os caminhos (local e CI)
    pacman_source = workspace / 'temp_pacman'
    if not pacman_source.exists():
        pacman_source = workspace / 'temp_pacman_source'
    
    if not pacman_source.exists():
        print(f"❌ Código fonte do Pacman não encontrado")
        print("💡 Execute: git clone https://github.com/abozanona/pacman-contribution-graph.git temp_pacman")
        print(f"   ou use temp_pacman_source")
        return
    
    print(f"📂 Usando código fonte em: {pacman_source}\n")
    
    # Atualiza o types.ts primeiro
    print("1️⃣  Atualizando types.ts...")
    if not update_types_file(pacman_source, celebration):
        print("❌ Falha ao atualizar types.ts")
        return
    
    # Atualiza o constants.ts
    print("\n2️⃣  Atualizando constants.ts...")
    if not update_constants_file(pacman_source, celebration, theme_data):
        print("❌ Falha ao atualizar constants.ts")
        return
    
    # Atualiza a action
    print("\n3️⃣  Atualizando GitHub Action...")
    if not generate_custom_action(pacman_source, celebration):
        print("❌ Falha ao atualizar action")
        return
    
    print(f"\n✅ Configuração concluída!")
    print(f"\n📋 Próximos passos:")
    print(f"   1. cd temp_pacman_source")
    print(f"   2. npm install")
    print(f"   3. npm run build")
    print(f"   4. cd github-action && npm install && npm run build")
    print(f"   5. Use a action local no seu workflow")
    
    # Salva informações do tema
    theme_info_path = workspace / 'scripts' / 'current_pacman_theme.json'
    theme_info = {
        'celebration': celebration,
        'theme': theme_data,
        'modified_files': [
            'temp_pacman_source/src/core/constants.ts',
            'temp_pacman_source/github-action/src/index.js'
        ]
    }
    theme_info_path.write_text(json.dumps(theme_info, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\n💾 Info do tema salva em: {theme_info_path}")


if __name__ == '__main__':
    main()

