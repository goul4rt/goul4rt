# 🔄 Fluxo CI/CD - Execução em Tempo Real

## 📋 Visão Geral

Todo o código do Pacman é **baixado e processado durante a execução do workflow** no GitHub Actions. **Nada é commitado** no repositório.

## 🚫 O que NÃO vai para o Git

```
❌ temp_pacman/          # Baixado no CI
❌ temp_pacman_source/   # Apenas para testes locais
❌ dist/                 # Gerado no CI
❌ node_modules/         # Dependências npm
❌ __pycache__/          # Cache Python
```

**Todos bloqueados pelo `.gitignore`**

## ✅ O que VAI para o Git

```
✅ .github/workflows/packman.yml        # Workflow principal
✅ scripts/pacman_theme_generator.py    # Gerador de temas
✅ scripts/custom_pacman_generator.py   # Aplicador de temas
✅ scripts/pacman_theme.json            # Tema atual (gerado)
✅ scripts/pacman_theme_previews/       # Previews dos temas
✅ scripts/*.md                         # Documentação
✅ .gitignore                           # Ignora temporários
```

## 🔄 Fluxo de Execução (GitHub Actions)

### Passo a Passo

```yaml
┌─────────────────────────────────────────────────────────┐
│ 1. TRIGGER                                              │
│    - Push, Schedule ou Manual                           │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 2. CHECKOUT                                             │
│    actions/checkout@v3                                  │
│    └─> Baixa: scripts/, .github/workflows/             │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 3. SETUP PYTHON                                         │
│    actions/setup-python@v4                              │
│    └─> Instala Python 3.x                               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 4. DETECTA TEMA                                         │
│    python3 scripts/pacman_theme_generator.py            │
│    └─> Gera: scripts/pacman_theme.json                  │
│        {                                                │
│          "celebration": "halloween",                    │
│          "theme": { cores... }                          │
│        }                                                │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 5. CLONE PACMAN (TEMPORÁRIO)                            │
│    git clone https://github.com/abozanona/...          │
│    └─> Cria: temp_pacman/ (APENAS NO CI)               │
│                                                         │
│    ⚠️  Este diretório existe APENAS durante a execução! │
│    ⚠️  Será deletado no step de cleanup                 │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 6. APLICA TEMA                                          │
│    python3 scripts/custom_pacman_generator.py halloween │
│    └─> Modifica temp_pacman/:                           │
│        ✓ temp_pacman/src/types.ts                       │
│        ✓ temp_pacman/src/core/constants.ts              │
│        ✓ temp_pacman/github-action/src/index.js         │
│                                                         │
│    ⚠️  Modificações APENAS em temp_pacman/ (temporário) │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 7. COPIA TEMA JSON                                      │
│    cp scripts/pacman_theme.json temp_pacman/scripts/    │
│    └─> Para que index.js possa ler o tema               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 8. BUILD BIBLIOTECA                                     │
│    cd temp_pacman                                       │
│    npm install                                          │
│    npm run build                                        │
│    └─> Compila TypeScript com tema customizado          │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 9. BUILD ACTION                                         │
│    cd temp_pacman/github-action                         │
│    npm install                                          │
│    npm run build                                        │
│    └─> Compila action customizada                       │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 10. GERA SVG                                            │
│     cd temp_pacman/github-action                        │
│     node dist/index.js                                  │
│     └─> Lê: ../../scripts/pacman_theme.json             │
│         Detecta: "halloween"                            │
│         Gera: dist/pacman-contribution-graph.svg        │
│               dist/pacman-contribution-graph-dark.svg   │
│                                                         │
│     🎨 SVG gerado com cores do Halloween!               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 11. COPIA SVGs                                          │
│     cp temp_pacman/github-action/dist/*.svg ./dist/     │
│     └─> Move SVGs para raiz do workspace                │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 12. CLEANUP                                             │
│     rm -rf temp_pacman                                  │
│     └─> ⚠️  DELETA tudo que foi baixado/gerado          │
│                                                         │
│     ✅ Workspace limpo, sem arquivos temporários         │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│ 13. DEPLOY (BRANCH OUTPUT)                              │
│     crazy-max/ghaction-github-pages@v3.1.0              │
│     └─> Push: dist/*.svg → branch 'output'              │
│                                                         │
│     📤 SVGs disponíveis publicamente!                    │
└─────────────────────────────────────────────────────────┘
```

## 🧪 Teste Local vs CI

### Teste Local (Desenvolvedor)

```bash
# Você pode testar localmente:
git clone https://github.com/abozanona/pacman-contribution-graph.git temp_pacman
python3 scripts/custom_pacman_generator.py halloween
cd temp_pacman && npm install && npm run build

# ⚠️  MAS NÃO COMMITE temp_pacman/
# Está no .gitignore!
```

### Execução CI (Automática)

```bash
# GitHub Actions faz tudo automaticamente:
1. Baixa temp_pacman/
2. Modifica arquivos
3. Builda
4. Gera SVGs
5. DELETA temp_pacman/
6. Push apenas dos SVGs para branch 'output'

# ✅ Nada de temporário vai para o repositório principal
```

## 📁 Estrutura do Repositório

### O que está no Git (Main Branch)

```
goul4rt/
├── .github/
│   └── workflows/
│       └── packman.yml              ✅ Commitado
├── scripts/
│   ├── pacman_theme_generator.py   ✅ Commitado
│   ├── custom_pacman_generator.py  ✅ Commitado
│   ├── pacman_theme.json           ✅ Commitado (gerado)
│   ├── pacman_theme_previews/      ✅ Commitado
│   └── *.md                        ✅ Commitado
├── README.md                        ✅ Commitado
└── .gitignore                       ✅ Commitado
```

### O que está no Git (Output Branch)

```
output/
├── pacman-contribution-graph.svg       ✅ Gerado pelo CI
└── pacman-contribution-graph-dark.svg  ✅ Gerado pelo CI
```

### O que NÃO está no Git

```
temp_pacman/         ❌ Bloqueado (.gitignore)
temp_pacman_source/  ❌ Bloqueado (.gitignore)
dist/                ❌ Bloqueado (.gitignore)
node_modules/        ❌ Bloqueado (.gitignore)
__pycache__/         ❌ Bloqueado (.gitignore)
```

## 🔒 Garantias de Segurança

### .gitignore

```gitignore
# Pacman temporary directories
temp_pacman/
temp_pacman_source/

# Build outputs
dist/
node_modules/

# Python cache
__pycache__/
```

### Cleanup Step no Workflow

```yaml
- name: Cleanup
  if: always()
  run: |
    rm -rf temp_pacman
    echo "🧹 Limpeza concluída"
```

**Garante que mesmo se o workflow falhar, o cleanup sempre roda**

## 💡 Por Que Esse Design?

### ✅ Vantagens

1. **Repositório Limpo**
   - Apenas código fonte e configurações
   - Sem dependências ou builds

2. **Sempre Atualizado**
   - Cada execução baixa código mais recente
   - Sem risco de código desatualizado

3. **Sem Conflitos**
   - Nenhum arquivo gerado vai para o git
   - Sem merge conflicts

4. **Reproduzível**
   - Qualquer um pode rodar o workflow
   - Resultado sempre o mesmo

5. **Eficiente**
   - Usa cache do GitHub Actions
   - Cleanup automático

### ❌ Se Commitássemos temp_pacman/

- ❌ 50+ MB de node_modules
- ❌ Código duplicado
- ❌ Desatualizado rapidamente
- ❌ Merge conflicts constantes
- ❌ Histórico Git poluído

## 🎯 Resumo

### O que acontece no CI:

```
1. Clone do repositório principal
2. Download de temp_pacman/ (temporário)
3. Modificação dos arquivos (em temp_pacman/)
4. Build (gera dist/ em temp_pacman/)
5. Geração dos SVGs
6. Cópia dos SVGs para ./dist/
7. Cleanup (deleta temp_pacman/)
8. Push dos SVGs para branch 'output'
```

### O que vai para o Git:

```
Main branch:
  ✅ Scripts Python
  ✅ Workflow YAML
  ✅ Documentação
  ✅ .gitignore

Output branch:
  ✅ SVGs gerados
```

### O que NÃO vai para o Git:

```
  ❌ temp_pacman/
  ❌ temp_pacman_source/
  ❌ dist/ (local)
  ❌ node_modules/
  ❌ Build artifacts
```

## 📊 Tempo de Execução

```
Total: ~5-8 minutos

1. Checkout:           ~5s
2. Setup:             ~10s
3. Detect theme:       ~3s
4. Clone Pacman:      ~10s
5. Apply theme:        ~2s
6. npm install:      ~120s (com cache: ~30s)
7. Build library:     ~45s
8. Build action:      ~30s
9. Generate SVG:      ~20s
10. Cleanup:           ~2s
11. Deploy:           ~10s
```

## 🎉 Resultado Final

**✅ Repositório limpo e organizado**
**✅ Workflow totalmente automático**
**✅ Sem arquivos temporários commitados**
**✅ SVGs gerados e deployados automaticamente**
**✅ Sistema sustentável e mantível**

---

**Data**: 31 de Outubro de 2025
**Status**: ✅ Arquitetura CI/CD Otimizada
**Tema Atual**: Halloween 🎃

