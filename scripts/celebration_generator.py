#!/usr/bin/env python3
"""
Script para gerar README.md com decorações comemorativas
"""

from datetime import datetime
from pathlib import Path

# Base README template
BASE_README = """<br clear="both">

<h3 align="center">👋 Hi there! I'm Goulart, Mobile Development Specialist</h3>

###

<div align="center">
  <p>Passionate about creating exceptional mobile experiences and cross-platform solutions</p>
</div>

###

<div align="center">
  <img src="https://streak-stats.demolab.com?user=goul4rt&locale=en&mode=daily&theme={theme}&hide_border=true&border_radius=10" height="180" alt="GitHub Streak" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=goul4rt&layout=compact&theme={theme}&hide_border=true&border_radius=10" height="180" alt="Most Used Languages" />
</div>

###

<img align="right" height="180" src="{gif_url}" />

###

<h3 align="left">💻 Technologies & Tools</h3>

<div align="left">
  <img src="https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React Native" />
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white" alt="Swift" />
  <img src="https://img.shields.io/badge/Kotlin-0095D5?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/Objective--C-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Objective-C" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/Jest-C21325?style=for-the-badge&logo=jest&logoColor=white" alt="Jest" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="Oracle" />
  <img src="https://img.shields.io/badge/Android_Studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white" alt="Android Studio" />
  <img src="https://img.shields.io/badge/Xcode-147EFB?style=for-the-badge&logo=xcode&logoColor=white" alt="Xcode" />
</div>

###

<div align="left">
  <h3>📱 About Me</h3>
  <p>Mobile developer with expertise in native and cross-platform development. Focused on creating high-performance, user-friendly applications with clean architecture and modern development practices.</p>
</div>

###

<br clear="both">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/goul4rt/goul4rt/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/goul4rt/goul4rt/output/pacman-contribution-graph.svg">
  <img alt="pacman contribution graph" src="https://raw.githubusercontent.com/goul4rt/goul4rt/output/pacman-contribution-graph.svg">
</picture>

###
"""

# Decorações para cada data comemorativa
CELEBRATIONS = {
    'halloween': {
        'dates': [(10, 31)],  # 31 de outubro
        'header': '🎃👻 <h3 align="center">Happy Halloween! 🦇🕷️</h3>\n<h3 align="center">Hi there! I\'m Goulart, Mobile Development Specialist</h3>\n<div align="center"><h4>🕸️ Trick or Treat? Let\'s code some spooky features! 🕸️</h4></div>',
        'theme': 'halloween',
        'gif_url': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHM1NTJrYmhhNnlrNnpoa3IyajQxcTNvMWNuMzc2azYxbXB5eGpjZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uHWzPe1dPgkEj2UXZb/giphy.gif',
        'footer': '\n\n<div align="center">\n  <h3>🎃 Happy Halloween! 🎃</h3>\n  <p>May your code be bug-free and your commits be clean! 👻</p>\n</div>\n'
    },
    'natal': {
        'dates': [(12, 24), (12, 25)],  # 24 e 25 de dezembro
        'header': '🎄🎅 <h3 align="center">Merry Christmas! ⛄🎁</h3>\n<h3 align="center">Hi there! I\'m Goulart, Mobile Development Specialist</h3>\n<div align="center"><h4>🌟 May your code compile and your bugs be few! 🌟</h4></div>',
        'theme': 'nord',
        'gif_url': 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3RxMnpkOXFseGNrbXVtb3V6OGM5eHFlb2FyeDFvMDFqejExMGJzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QaYqakQZPUdUv1YG2a/giphy.gif',
        'footer': '\n\n<div align="center">\n  <h3>🎄 Merry Christmas! 🎄</h3>\n  <p>Wishing you clean code and successful deployments! 🎅</p>\n</div>\n'
    },
    'ano_novo': {
        'dates': [(1, 1), (12, 31)],  # 31 de dezembro e 1 de janeiro
        'header': '🎆🎊 <h3 align="center">Happy New Year! 🥳🎉</h3>\n<h3 align="center">Hi there! I\'m Goulart, Mobile Development Specialist</h3>\n<div align="center"><h4>✨ New year, new commits, new features! ✨</h4></div>',
        'theme': 'radical',
        'gif_url': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjIxNTBoN2lmaGZra2dlcGJhanNuaHg0aGYxNzU2ODR6emEwcnpmdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QMkPpxPDYY0fu/giphy.gif',
        'footer': '\n\n<div align="center">\n  <h3>🎊 Happy New Year! 🎊</h3>\n  <p>Here\'s to another year of amazing code! 🚀</p>\n</div>\n'
    },
    'programador': {
        'dates': [(9, 13)],  # 13 de setembro - Dia do Programador
        'header': '💻🚀 <h3 align="center">Happy Programmer\'s Day! 👨‍💻👩‍💻</h3>\n<h3 align="center">Hi there! I\'m Goulart, Mobile Development Specialist</h3>\n<div align="center"><h4>🎯 Celebrating the art of coding! 🎯</h4></div>',
        'theme': 'synthwave',
        'gif_url': 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3o2czVqNjdzOTh4cnFidzk2a2Y1ZXZ1OWl3c2N0ZWdlNnpwdWM2dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zOvBKUUEERdNm/giphy.gif',
        'footer': '\n\n<div align="center">\n  <h3>💻 Programmer\'s Day! 💻</h3>\n  <p>Keep calm and code on! 🚀</p>\n</div>\n'
    },
    'independencia': {
        'dates': [(9, 7)],  # 7 de setembro
        'header': '🇧🇷 <h3 align="center">Independência do Brasil! 🟢🟡</h3>\n<h3 align="center">Hi there! I\'m Goulart, Mobile Development Specialist</h3>\n<div align="center"><h4>💚 Desenvolvendo o futuro do Brasil! 💛</h4></div>',
        'theme': 'chartreuse-dark',
        'gif_url': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjdjMnJqNW1veTlybjhhOWR1OHFic2U3YjR0eHJiMXJwdWF1cHd5byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1wmOUUYKe1CpOLFjE3/giphy.gif',
        'footer': '\n\n<div align="center">\n  <h3>🇧🇷 Independence Day! 🇧🇷</h3>\n  <p>Coding with pride Brazilian! 💚💛</p>\n</div>\n'
    },
    'carnaval': {
        'dates': [(2, 12), (2, 13), (2, 14)],  # Datas aproximadas - variam
        'header': '🎭🎊 <h3 align="center">Happy Carnival! 🎉🎺</h3>\n<h3 align="center">Hi there! I\'m Goulart, Mobile Development Specialist</h3>\n<div align="center"><h4>🎵 It\'s time to code and samba! 🎵</h4></div>',
        'theme': 'radical',
        'gif_url': 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXZxZmZ1ZnJ5bnV5OGNkb3NjdnN5bnl5ZnJ5Y3lmcnlmcnlmcnlmcnkmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/l0MYt5jPR6QX5pnqM/giphy.gif',
        'footer': '\n\n<div align="center">\n  <h3>🎊 Happy Carnival! 🎊</h3>\n  <p>Enjoy, Dance, Code! 🎭</p>\n</div>\n'
    }
}

# Tema e GIF padrão
DEFAULT_THEME = 'tokyonight'
DEFAULT_GIF = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDhsNDM1YWt5OHYzbTVoamRyMW1kZzJncTJobXA2c2Q4Y2VpMXVnZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/82nxC1u2BC8VU1wiZq/giphy.gif'


def get_current_celebration():
    """Retorna a celebração atual baseada na data de hoje"""
    now = datetime.now()
    current_date = (now.month, now.day)
    
    for celebration_name, celebration_data in CELEBRATIONS.items():
        if current_date in celebration_data['dates']:
            return celebration_data
    
    return None


def generate_readme():
    """Gera o README.md com ou sem decoração comemorativa"""
    celebration = get_current_celebration()
    
    if celebration:
        # Modo comemorativo
        theme = celebration['theme']
        gif_url = celebration['gif_url']
        
        # Substitui o header padrão pelo comemorativo
        readme = celebration['header'] + '\n\n###\n\n'
        
        # Adiciona o resto do conteúdo
        readme += BASE_README.split('###\n\n', 2)[2]
        
        # Formata com tema e GIF certos
        readme = readme.format(theme=theme, gif_url=gif_url)
        
        # Adiciona footer comemorativo
        readme += celebration['footer']
    else:
        # Modo normal
        readme = BASE_README.format(theme=DEFAULT_THEME, gif_url=DEFAULT_GIF)
        
        # Adiciona header padrão
        readme = readme.replace(
            '<h3 align="center">👋 Hi there!',
            '<h3 align="center">👋 Hi there!'
        )
    
    return readme


def main():
    """Função principal"""
    print("🎨 Gerando README com decorações comemorativas...")
    
    readme_content = generate_readme()
    
    # Caminho do README
    readme_path = Path(__file__).parent.parent / 'README.md'
    
    # Escreve o README
    readme_path.write_text(readme_content, encoding='utf-8')
    
    celebration = get_current_celebration()
    if celebration:
        print(f"✨ README atualizado com decoração comemorativa!")
    else:
        print("📄 README atualizado (sem decoração especial hoje)")


if __name__ == '__main__':
    main()

