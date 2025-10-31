# 🎮 Customização de Cores do Pacman Contribution Graph

Este sistema permite customizar as cores do Pacman Contribution Graph de acordo com celebrações e datas comemorativas!

## 🎨 Como Funciona

O sistema tem 3 componentes principais:

### 1. **Gerador de Temas** (`pacman_theme_generator.py`)
Detecta a data atual e seleciona o tema apropriado com cores customizadas.

```bash
# Ver todos os temas disponíveis
python3 scripts/pacman_theme_generator.py --list

# Gerar tema atual (baseado na data)
python3 scripts/pacman_theme_generator.py

# Gerar previews de todos os temas
python3 scripts/pacman_theme_generator.py --generate-all
```

### 2. **Aplicador de Temas** (`custom_pacman_generator.py`)
Modifica o código fonte do Pacman para usar os temas customizados.

```bash
# Aplicar tema atual
python3 scripts/custom_pacman_generator.py

# Aplicar tema específico
python3 scripts/custom_pacman_generator.py halloween
python3 scripts/custom_pacman_generator.py natal
```

### 3. **Integração com Workflow**
O workflow GitHub Actions gera automaticamente o gráfico com o tema correto.

## 🎯 Temas Disponíveis

Todos os temas são sincronizados com o `celebration_generator.py`:

| Celebração | Cores Principais | Período |
|------------|------------------|---------|
| 🎃 Halloween | Laranja + Roxo | 31 de Outubro |
| 🎄 Natal | Azul Frio (Nord) | 24-25 de Dezembro |
| 🎊 Ano Novo | Rosa Neon | 31 Dez - 1 Jan |
| 💻 Programador | Synthwave Neon | 13 de Setembro |
| 🇧🇷 Independência | Verde + Amarelo | 7 de Setembro |
| 🎭 Carnaval | Cores Vibrantes | 12-14 de Fevereiro |
| 🌽 São João | Tons Quentes | 23-24 de Junho |
| ⚔️ Star Wars | Roxo + Verde | 4 de Maio |
| 🥧 Pi Day | Azul Matemático | 14 de Março |
| 👩‍💻 Grace Hopper | OneDark | 9 de Dezembro |
| 🎮 Video Game | Dracula | 29 de Agosto |
| 💘 Valentine's | Rosa Amor | 14 de Fevereiro |
| 🤡 April Fools | Cores Malucas | 1 de Abril |
| 🔭 Towel Day | Cobalt | 25 de Maio |
| ⚡ Back to Future | Synthwave | 21 de Outubro |
| 🌍 Earth Day | Verde Natureza | 22 de Abril |
| 🌙 Default | Tokyo Night | Outros dias |

## 📋 Estrutura dos Temas

Cada tema tem as seguintes propriedades:

```json
{
  "textColor": "#ff6b35",          // Cor dos labels (meses)
  "gridBackground": "#1a1423",     // Cor de fundo do grid
  "wallColor": "#ff6b35",          // Cor das paredes
  "intensityColors": [             // 5 cores para níveis de contribuição
    "#2d1b2e",  // NONE (sem contribuições)
    "#5c3d5e",  // FIRST_QUARTILE (poucas)
    "#9b4f8e",  // SECOND_QUARTILE (moderadas)
    "#ff6b35",  // THIRD_QUARTILE (muitas)
    "#ffa500"   // FOURTH_QUARTILE (excepcionais)
  ],
  "pacmanColor": "#ffa500",        // Cor do Pac-Man
  "description": "🎃 Descrição"
}
```

## 🚀 Setup Inicial

### Passo 1: Clonar o código fonte do Pacman

```bash
git clone https://github.com/abozanona/pacman-contribution-graph.git temp_pacman_source
```

### Passo 2: Instalar dependências

```bash
cd temp_pacman_source
npm install

cd github-action
npm install
```

### Passo 3: Aplicar tema customizado

```bash
cd ..
python3 scripts/custom_pacman_generator.py
```

### Passo 4: Buildar

```bash
cd temp_pacman_source
npm run build

cd github-action
npm run build
```

## 🔧 Uso Local (para testar)

Depois de buildar, você pode usar a biblioteca localmente:

```javascript
import { PacmanRenderer } from './temp_pacman_source/dist/index.js';

const renderer = new PacmanRenderer({
    platform: "github",
    username: "seu_usuario",
    outputFormat: "svg",
    gameSpeed: 1,
    gameTheme: "halloween",  // Seu tema customizado!
    githubSettings: {
        accessToken: "seu_token"
    }
});

renderer.start();
```

## 🎭 Adicionar Novo Tema

### 1. Edite `pacman_theme_generator.py`

```python
PACMAN_THEMES = {
    # ... outros temas ...
    'meu_tema': {
        'textColor': '#FFFFFF',
        'gridBackground': '#000000',
        'wallColor': '#FF0000',
        'intensityColors': ['#111', '#333', '#555', '#777', '#999'],
        'pacmanColor': '#FFFF00',
        'description': '🎨 Meu Tema Personalizado'
    }
}

CELEBRATION_DATES = {
    # ... outras datas ...
    'meu_tema': [(3, 15)]  # 15 de março
}
```

### 2. Regenere os temas

```bash
python3 scripts/pacman_theme_generator.py --generate-all
```

### 3. Aplique o tema

```bash
python3 scripts/custom_pacman_generator.py meu_tema
```

## 🔄 Integração com Workflow

Para usar no GitHub Actions, você tem duas opções:

### Opção 1: Fork do Pacman (Recomendado)

1. Faça fork do repositório `pacman-contribution-graph`
2. Aplique seus temas customizados
3. Faça commit e push
4. Use seu fork no workflow:

```yaml
- name: generate pacman-contribution-graph.svg
  uses: SEU_USUARIO/pacman-contribution-graph@main
  with:
    github_user_name: ${{ github.repository_owner }}
```

### Opção 2: Action Local

1. Copie o código buildado para `.github/actions/pacman-custom/`
2. Use no workflow:

```yaml
- name: generate pacman-contribution-graph.svg
  uses: ./.github/actions/pacman-custom
  with:
    github_user_name: ${{ github.repository_owner }}
```

## 📊 Preview dos Temas

Todos os temas têm arquivos de preview em `scripts/pacman_theme_previews/`:

```bash
# Ver tema específico
cat scripts/pacman_theme_previews/theme_halloween.json

# Ver tema atual
cat scripts/pacman_theme.json
```

## 🎨 Paleta de Cores

Para criar temas harmoniosos, considere:

### Ferramentas de Cores
- [Coolors.co](https://coolors.co/) - Gerador de paletas
- [Adobe Color](https://color.adobe.com/) - Roda de cores
- [ColorHunt](https://colorhunt.co/) - Paletas prontas

### Dicas
- Use 5 tons da mesma família para `intensityColors`
- Cores mais escuras = menos contribuições
- Cores mais claras/vibrantes = mais contribuições
- `pacmanColor` deve contrastar com o background
- `wallColor` deve ter boa visibilidade

## 🐛 Troubleshooting

### Tema não aparece no constants.ts
- Verifique se o arquivo `temp_pacman_source/src/core/constants.ts` existe
- O script procura por `'gitlab-dark': {` como marcador

### Build falha
```bash
# Limpe e reinstale
cd temp_pacman_source
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Cores não mudam
- Certifique-se de buildar após modificar: `npm run build`
- Limpe o cache do navegador se testando localmente
- Verifique se o tema foi adicionado corretamente ao constants.ts

## 📚 Referências

- [Pacman Contribution Graph Original](https://github.com/abozanona/pacman-contribution-graph)
- [GitHub Stats Themes](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md)
- [Sistema de Celebrações](./README.md)

## 🤝 Contribuindo

Para adicionar novos temas ou melhorar os existentes:

1. Teste localmente primeiro
2. Documente as cores escolhidas
3. Adicione preview do tema
4. Mantenha consistência com `celebration_generator.py`

---

**Feito com 💜 para deixar seu perfil GitHub mais colorido!**

