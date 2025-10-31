#!/usr/bin/env python3
"""
Script para gerar todos os READMEs com diferentes celebrações para visualização
"""

from pathlib import Path
from celebration_generator import CELEBRATIONS, BASE_README, DEFAULT_THEME, DEFAULT_GIF


def generate_readme_for_celebration(celebration_data):
    """Gera README para uma celebração específica"""
    theme = celebration_data['theme']
    gif_url = celebration_data['gif_url']
    
    # Substitui o header padrão pelo comemorativo
    readme = celebration_data['header'] + '\n\n###\n\n'
    
    # Adiciona o resto do conteúdo
    readme += BASE_README.split('###\n\n', 2)[2]
    
    # Formata com tema e GIF certos
    readme = readme.format(theme=theme, gif_url=gif_url)
    
    # Adiciona footer comemorativo
    readme += celebration_data['footer']
    
    return readme


def generate_default_readme():
    """Gera README padrão (sem celebração)"""
    return BASE_README.format(theme=DEFAULT_THEME, gif_url=DEFAULT_GIF)


def main():
    """Função principal"""
    print("🎨 Gerando todos os READMEs para visualização...\n")
    
    # Diretório de saída
    output_dir = Path(__file__).parent / 'preview_readmes'
    output_dir.mkdir(exist_ok=True)
    
    # Gera README padrão
    default_readme = generate_default_readme()
    default_path = output_dir / 'README_default.md'
    default_path.write_text(default_readme, encoding='utf-8')
    print(f"✅ README padrão: {default_path}")
    
    # Gera README para cada celebração
    for celebration_name, celebration_data in CELEBRATIONS.items():
        readme_content = generate_readme_for_celebration(celebration_data)
        
        # Salva em arquivo
        filename = f'README_{celebration_name}.md'
        file_path = output_dir / filename
        file_path.write_text(readme_content, encoding='utf-8')
        
        dates_str = ', '.join([f"{d[1]:02d}/{d[0]:02d}" for d in celebration_data['dates']])
        print(f"✅ README {celebration_name}: {file_path}")
        print(f"   📅 Datas: {dates_str}")
        print(f"   🎨 Tema: {celebration_data['theme']}\n")
    
    print(f"\n🎉 Todos os READMEs foram gerados em: {output_dir}")
    print(f"📂 Total de arquivos: {len(CELEBRATIONS) + 1} (incluindo o padrão)")


if __name__ == '__main__':
    main()

