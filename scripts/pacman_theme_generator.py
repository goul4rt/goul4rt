#!/usr/bin/env python3
"""
Script para gerar temas customizados do Pacman baseado em celebrações
Mapeia os temas do GitHub Stats para cores específicas do Pacman
"""

from datetime import datetime
from pathlib import Path
import json

# Mapeamento de celebrações para temas do Pacman
# Cada tema tem: textColor, gridBackground, wallColor, intensityColors (array de 5 cores)
PACMAN_THEMES = {
    'halloween': {
        'textColor': '#ff6b35',
        'gridBackground': '#1a1423',
        'wallColor': '#ff6b35',
        'intensityColors': ['#2d1b2e', '#5c3d5e', '#9b4f8e', '#ff6b35', '#ffa500'],
        'pacmanColor': '#ffa500',
        'description': '🎃 Tema de Halloween - Laranja e Roxo Assustador'
    },
    'natal': {
        'textColor': '#88c0d0',
        'gridBackground': '#2e3440',
        'wallColor': '#88c0d0',
        'intensityColors': ['#2e3440', '#3b4252', '#5e81ac', '#88c0d0', '#8fbcbb'],
        'pacmanColor': '#bf616a',
        'description': '🎄 Tema de Natal - Nord (Azul Frio)'
    },
    'ano_novo': {
        'textColor': '#f55e7e',
        'gridBackground': '#141321',
        'wallColor': '#fe428e',
        'intensityColors': ['#141321', '#3a1f5d', '#fe428e', '#a9fef7', '#f8d847'],
        'pacmanColor': '#f8d847',
        'description': '🎊 Tema de Ano Novo - Radical (Rosa Neon)'
    },
    'programador': {
        'textColor': '#e2e9ec',
        'gridBackground': '#2b213a',
        'wallColor': '#ff7edb',
        'intensityColors': ['#2b213a', '#495495', '#72f1b8', '#ff7edb', '#e2e9ec'],
        'pacmanColor': '#ff7edb',
        'description': '💻 Dia do Programador - Synthwave (Neon Retrô)'
    },
    'independencia': {
        'textColor': '#7fff00',
        'gridBackground': '#0d1117',
        'wallColor': '#7fff00',
        'intensityColors': ['#0d1117', '#1b3a0f', '#2d5f1f', '#4f9f2f', '#7fff00'],
        'pacmanColor': '#ffd700',
        'description': '🇧🇷 Independência - Verde e Amarelo Brasil'
    },
    'carnaval': {
        'textColor': '#fe428e',
        'gridBackground': '#141321',
        'wallColor': '#f8d847',
        'intensityColors': ['#141321', '#3a1f5d', '#fe428e', '#f8d847', '#a9fef7'],
        'pacmanColor': '#f8d847',
        'description': '🎭 Carnaval - Radical (Cores Vibrantes)'
    },
    'sao_joao': {
        'textColor': '#859900',
        'gridBackground': '#002b36',
        'wallColor': '#cb4b16',
        'intensityColors': ['#002b36', '#073642', '#586e75', '#cb4b16', '#dc322f'],
        'pacmanColor': '#b58900',
        'description': '🌽 São João - Solarized Dark (Tons Quentes)'
    },
    'star_wars': {
        'textColor': '#7a5cff',
        'gridBackground': '#000000',
        'wallColor': '#7a5cff',
        'intensityColors': ['#000000', '#1f1f3a', '#4a3e8c', '#7a5cff', '#8b4cff'],
        'pacmanColor': '#3aff62',
        'description': '⚔️ Star Wars Day - Midnight Purple (Força)'
    },
    'pi_day': {
        'textColor': '#00aeff',
        'gridBackground': '#050f2c',
        'wallColor': '#00aeff',
        'intensityColors': ['#050f2c', '#003f88', '#0062c9', '#00aeff', '#5de0ff'],
        'pacmanColor': '#5de0ff',
        'description': '🥧 Pi Day - Algolia (Azul Matemático)'
    },
    'grace_hopper': {
        'textColor': '#abb2bf',
        'gridBackground': '#282c34',
        'wallColor': '#61afef',
        'intensityColors': ['#282c34', '#3e4451', '#528bff', '#61afef', '#98c379'],
        'pacmanColor': '#c678dd',
        'description': '👩‍💻 Grace Hopper - OneDark (Programadora)'
    },
    'video_game_day': {
        'textColor': '#f8f8f2',
        'gridBackground': '#282a36',
        'wallColor': '#ff79c6',
        'intensityColors': ['#282a36', '#44475a', '#6272a4', '#bd93f9', '#ff79c6'],
        'pacmanColor': '#ffb86c',
        'description': '🎮 Video Game Day - Dracula (Gamer)'
    },
    'valentines': {
        'textColor': '#ff3860',
        'gridBackground': '#ffffff',
        'wallColor': '#ff3860',
        'intensityColors': ['#f5f5f5', '#ffb3d9', '#ff8fd4', '#ff6bcb', '#ff3860'],
        'pacmanColor': '#ff1744',
        'description': '💘 Valentine\'s Day - Buefy (Rosa Amor)'
    },
    'april_fools': {
        'textColor': '#fe428e',
        'gridBackground': '#141321',
        'wallColor': '#f8d847',
        'intensityColors': ['#141321', '#3a1f5d', '#fe428e', '#f8d847', '#a9fef7'],
        'pacmanColor': '#00ff00',
        'description': '🤡 April Fools - Radical (Cores Malucas)'
    },
    'towel_day': {
        'textColor': '#6fb3d2',
        'gridBackground': '#193549',
        'wallColor': '#6fb3d2',
        'intensityColors': ['#193549', '#1f4662', '#3d566e', '#6fb3d2', '#82d8ff'],
        'pacmanColor': '#ffc600',
        'description': '🔭 Towel Day - Cobalt (Don\'t Panic!)'
    },
    'back_future': {
        'textColor': '#e2e9ec',
        'gridBackground': '#2b213a',
        'wallColor': '#ff7edb',
        'intensityColors': ['#2b213a', '#495495', '#72f1b8', '#ff7edb', '#e2e9ec'],
        'pacmanColor': '#ffd700',
        'description': '⚡ Back to Future - Synthwave (88mph)'
    },
    'earth_day': {
        'textColor': '#81c995',
        'gridBackground': '#1c1f29',
        'wallColor': '#81c995',
        'intensityColors': ['#1c1f29', '#2f3f4f', '#4a6f5f', '#6fa87f', '#81c995'],
        'pacmanColor': '#8bc34a',
        'description': '🌍 Earth Day - Apprentice (Verde Natureza)'
    },
    'default': {
        'textColor': '#7aa2f7',
        'gridBackground': '#1a1b26',
        'wallColor': '#bb9af7',
        'intensityColors': ['#1a1b26', '#24283b', '#414868', '#565f89', '#7aa2f7'],
        'pacmanColor': '#f7ca88',
        'description': '🌙 Default - Tokyo Night'
    }
}

# Datas das celebrações (mesmo do celebration_generator.py)
CELEBRATION_DATES = {
    'halloween': [(10, 31)],
    'natal': [(12, 24), (12, 25)],
    'ano_novo': [(1, 1), (12, 31)],
    'programador': [(9, 13)],
    'independencia': [(9, 7)],
    'carnaval': [(2, 12), (2, 13), (2, 14)],
    'sao_joao': [(6, 23), (6, 24)],
    'star_wars': [(5, 4)],
    'pi_day': [(3, 14)],
    'grace_hopper': [(12, 9)],
    'video_game_day': [(8, 29)],
    'valentines': [(2, 14)],
    'april_fools': [(4, 1)],
    'towel_day': [(5, 25)],
    'back_future': [(10, 21)],
    'earth_day': [(4, 22)]
}


def get_current_celebration_theme():
    """Retorna o tema da celebração atual baseado na data de hoje"""
    now = datetime.now()
    current_date = (now.month, now.day)
    
    for celebration_name, dates in CELEBRATION_DATES.items():
        if current_date in dates:
            return celebration_name, PACMAN_THEMES[celebration_name]
    
    return 'default', PACMAN_THEMES['default']


def generate_theme_json(output_path=None):
    """Gera arquivo JSON com o tema atual"""
    celebration_name, theme_data = get_current_celebration_theme()
    
    output = {
        'celebration': celebration_name,
        'theme': theme_data,
        'generated_at': datetime.now().isoformat(),
        'date': f"{datetime.now().month}/{datetime.now().day}"
    }
    
    if output_path:
        output_file = Path(output_path)
        output_file.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"✅ Tema gerado: {celebration_name}")
        print(f"📝 Descrição: {theme_data['description']}")
        print(f"💾 Arquivo salvo em: {output_file}")
    
    return output


def list_all_themes():
    """Lista todos os temas disponíveis"""
    print("🎨 Temas Disponíveis do Pacman:\n")
    for name, theme in PACMAN_THEMES.items():
        print(f"  {name:20} - {theme['description']}")


def generate_all_theme_previews():
    """Gera arquivos JSON de preview para todos os temas"""
    preview_dir = Path(__file__).parent / 'pacman_theme_previews'
    preview_dir.mkdir(exist_ok=True)
    
    for name, theme in PACMAN_THEMES.items():
        output = {
            'celebration': name,
            'theme': theme,
            'generated_at': datetime.now().isoformat()
        }
        
        output_file = preview_dir / f"theme_{name}.json"
        output_file.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
    
    print(f"✅ {len(PACMAN_THEMES)} temas salvos em: {preview_dir}")


def main():
    """Função principal"""
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--list':
            list_all_themes()
            return
        elif sys.argv[1] == '--generate-all':
            generate_all_theme_previews()
            return
    
    # Gera tema atual
    print("🎮 Gerando tema Pacman baseado na data atual...")
    
    # Caminho do arquivo de saída
    output_path = Path(__file__).parent / 'pacman_theme.json'
    
    theme_data = generate_theme_json(output_path)
    
    if theme_data['celebration'] != 'default':
        print(f"\n🎉 Celebração detectada! Usando tema especial.")
    else:
        print(f"\n📅 Nenhuma celebração hoje. Usando tema padrão.")


if __name__ == '__main__':
    main()

