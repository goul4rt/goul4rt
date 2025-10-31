# 🚀 Quick Start - Pacman com Cores Customizadas

## Resultado

Ao final deste guia, você terá um Pacman Contribution Graph com cores que mudam automaticamente de acordo com datas comemorativas! 🎨🎮

### O que foi criado hoje (31 de Outubro):

```json
{
  "celebration": "halloween",
  "theme": {
    "textColor": "#ff6b35",           // Laranja vibrante
    "gridBackground": "#1a1423",      // Roxo escuro
    "wallColor": "#ff6b35",           // Laranja
    "intensityColors": [
      "#2d1b2e",  // Muito escuro (sem contribuições)
      "#5c3d5e",  // Roxo escuro
      "#9b4f8e",  // Roxo médio
      "#ff6b35",  // Laranja
      "#ffa500"   // Laranja brilhante (muitas contribuições)
    ],
    "pacmanColor": "#ffa500"  // Pac-Man laranja 🎃
  }
}
```

## 🎯 Visão Geral

O sistema tem 3 componentes:

1. **`pacman_theme_generator.py`** - Detecta a data e gera o tema
2. **`custom_pacman_generator.py`** - Aplica o tema no código do Pacman
3. **Código fonte modificado** - Pacman com os novos temas

## 📦 Arquivos Gerados

```
scripts/
├── pacman_theme_generator.py     # ✅ Gerador de temas
├── custom_pacman_generator.py    # ✅ Aplicador de temas
├── pacman_theme.json             # ✅ Tema atual (Halloween)
├── current_pacman_theme.json     # ✅ Info do tema aplicado
└── pacman_theme_previews/        # ✅ 17 temas em preview
    ├── theme_halloween.json
    ├── theme_natal.json
    ├── theme_ano_novo.json
    └── ... (14 outros temas)

temp_pacman_source/               # ✅ Código fonte clonado
└── src/core/constants.ts         # ✅ MODIFICADO com tema Halloween
```

## 🎨 Teste Rápido dos Temas

```bash
# Ver todos os temas disponíveis
python3 scripts/pacman_theme_generator.py --list

# Ver tema atual (detectado pela data)
python3 scripts/pacman_theme_generator.py

# Ver preview de um tema específico
cat scripts/pacman_theme_previews/theme_halloween.json
```

## 🔧 Como Usar

### Opção 1: Tema Automático (Recomendado)

O tema muda automaticamente baseado na data:

```bash
# 1. Gera tema atual
python3 scripts/pacman_theme_generator.py

# 2. Aplica no código do Pacman
python3 scripts/custom_pacman_generator.py
```

### Opção 2: Tema Específico

Forçar um tema específico:

```bash
# Aplicar tema de Natal (mesmo que não seja Natal)
python3 scripts/custom_pacman_generator.py natal

# Aplicar tema de Ano Novo
python3 scripts/custom_pacman_generator.py ano_novo

# Aplicar tema padrão
python3 scripts/custom_pacman_generator.py default
```

## 🏗️ Build do Pacman (Opcional)

Se você quiser gerar os SVGs localmente:

```bash
# 1. Instalar dependências
cd temp_pacman_source
npm install

# 2. Build da biblioteca
npm run build

# 3. Build da GitHub Action
cd github-action
npm install
npm run build
```

## 📅 Calendário de Temas

| Data | Tema | Cores Principais |
|------|------|------------------|
| **Hoje (31/10)** | 🎃 **Halloween** | **Laranja + Roxo** |
| 24-25/12 | 🎄 Natal | Azul Frio |
| 31/12 - 01/01 | 🎊 Ano Novo | Rosa Neon |
| 07/09 | 🇧🇷 Independência | Verde + Amarelo |
| 13/09 | 💻 Programador | Synthwave |
| 04/05 | ⚔️ Star Wars | Roxo + Verde |
| ... | ... | ... |

**Total: 17 temas** (16 celebrações + 1 default)

## 🎭 Comparação Visual

### Antes (GitHub Padrão)
- Verde claro para todas as contribuições
- Fundo branco ou preto simples

### Depois (Temas Customizados)
- **Halloween**: Laranja vibrante, roxo escuro, atmosfera assustadora 🎃
- **Natal**: Azul frio nórdico, clima de inverno ❄️
- **Ano Novo**: Rosa neon, cores de festa 🎉
- **Star Wars**: Roxo + Verde sabre de luz ⚔️
- ... e mais 13 temas!

## 💡 Como Funciona

### 1. Detecção da Data
```python
now = datetime.now()
current_date = (now.month, now.day)  # Ex: (10, 31) = Halloween

if current_date in celebration_dates:
    use_special_theme()
else:
    use_default_theme()
```

### 2. Aplicação das Cores
```typescript
// Antes (constants.ts original)
'github-dark': {
    textColor: '#8b949e',
    gridBackground: '#0d1117',
    wallColor: '#ffffff',
    intensityColors: ['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353']
}

// Depois (com tema Halloween adicionado)
'halloween': {
    textColor: '#ff6b35',
    gridBackground: '#1a1423',
    wallColor: '#ff6b35',
    intensityColors: ['#2d1b2e', '#5c3d5e', '#9b4f8e', '#ff6b35', '#ffa500']
}
```

### 3. Sincronização com celebration_generator.py
Ambos os scripts usam as **mesmas datas** para consistência visual no perfil!

## 🔄 Próximos Passos

### Usar Localmente
```bash
# Você já pode usar! O tema Halloween está aplicado
# Faça o build e teste localmente
cd temp_pacman_source
npm run build
```

### Integrar com GitHub Actions
Você tem duas opções:

**Opção A: Fork do Repositório (Melhor)**
1. Fazer fork de `abozanona/pacman-contribution-graph`
2. Aplicar seus temas customizados
3. Usar seu fork no workflow

**Opção B: Action Local (Mais Rápido)**
1. Copiar `temp_pacman_source/github-action/` para `.github/actions/pacman/`
2. Modificar workflow para usar action local

## 🎨 Adicionar Novo Tema

```bash
# 1. Edite pacman_theme_generator.py e adicione:
PACMAN_THEMES = {
    'meu_tema': {
        'textColor': '#FFFFFF',
        'gridBackground': '#000000',
        'wallColor': '#FF0000',
        'intensityColors': ['#111', '#333', '#555', '#777', '#999'],
        'pacmanColor': '#FFFF00',
        'description': '🎨 Meu Tema'
    }
}

CELEBRATION_DATES = {
    'meu_tema': [(3, 15)]  # 15 de março
}

# 2. Regenere
python3 scripts/pacman_theme_generator.py --generate-all

# 3. Aplique
python3 scripts/custom_pacman_generator.py meu_tema
```

## 📊 Status Atual

✅ **Concluído:**
- [x] 17 temas definidos com cores harmoniosas
- [x] Gerador automático baseado em data
- [x] Aplicador que modifica constants.ts
- [x] Sincronização com celebration_generator.py
- [x] Tema Halloween aplicado e testado
- [x] Preview de todos os temas gerados

⏳ **Próximo (Opcional):**
- [ ] Build da biblioteca Pacman
- [ ] Fork do repositório original
- [ ] Integração com GitHub Actions
- [ ] Deploy automático

## 🐛 Troubleshooting

### "Tema não foi aplicado"
```bash
# Verifique se o arquivo foi modificado
cat temp_pacman_source/src/core/constants.ts | grep halloween
# Deve mostrar o tema Halloween
```

### "Quero voltar ao original"
```bash
# Remova e clone novamente
rm -rf temp_pacman_source
git clone https://github.com/abozanona/pacman-contribution-graph.git temp_pacman_source
```

### "Como testar sem fazer build?"
```bash
# Veja os arquivos JSON gerados
cat scripts/pacman_theme.json
cat scripts/current_pacman_theme.json
cat scripts/pacman_theme_previews/theme_halloween.json
```

## 📚 Documentação Completa

- **[PACMAN_CUSTOMIZATION.md](./PACMAN_CUSTOMIZATION.md)** - Guia completo
- **[README.md](./README.md)** - Sistema de celebrações
- **[CELEBRATION_IDEAS.md](./CELEBRATION_IDEAS.md)** - Ideias de novas celebrações

## 🎉 Pronto!

Você agora tem um sistema completo de customização de cores do Pacman Contribution Graph! 🎮✨

**Hoje é Halloween** 🎃, então seu Pacman já está com o tema assustador de laranja e roxo aplicado!

Para testar outros temas:
```bash
python3 scripts/custom_pacman_generator.py natal     # 🎄 Azul frio
python3 scripts/custom_pacman_generator.py star_wars # ⚔️ Roxo + Verde
python3 scripts/custom_pacman_generator.py programador # 💻 Synthwave
```

---

**Feito com 💜 by Goulart - Happy Halloween! 🎃**

