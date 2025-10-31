# 🤖 Workflow Automático - Sistema Completo

## ✨ O que Acontece Automaticamente

O workflow `packman.yml` agora faz **TUDO automaticamente**:

### 🔄 Fluxo Completo (Sem Intervenção Manual)

```
┌─────────────────────────────────────────────┐
│  1. Trigger (Push/Schedule/Manual)          │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  2. Checkout & Setup Python                 │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  3. Detecta Tema Atual (Python)             │
│     • Executa pacman_theme_generator.py     │
│     • Identifica celebração (Halloween)     │
│     • Extrai cores do tema                  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  4. Clone Repositório Original              │
│     git clone pacman-contribution-graph     │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  5. Aplica Tema Customizado                 │
│     • Executa custom_pacman_generator.py    │
│     • Modifica constants.ts                 │
│     • Atualiza index.js                     │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  6. Build Automático                        │
│     • npm install (biblioteca)              │
│     • npm run build                         │
│     • npm install (action)                  │
│     • npm run build (action)                │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  7. Gera SVG com Tema                       │
│     • Executa action modificada             │
│     • Gera pacman-contribution-graph.svg    │
│     • Gera pacman-contribution-graph-dark   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  8. Push para Branch Output                 │
│     • SVGs disponíveis publicamente         │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  9. Cleanup & Logs                          │
│     • Remove temp_pacman                    │
│     • Mostra resumo                         │
└─────────────────────────────────────────────┘
```

## 🎃 Exemplo: Halloween (Hoje)

### Input
- **Data**: 31 de Outubro
- **Usuário**: Não precisa fazer nada

### Processamento Automático

```bash
# 1. Detecção
python3 scripts/pacman_theme_generator.py
# Output: halloween, #ff6b35, #1a1423, ...

# 2. Clone
git clone https://github.com/abozanona/pacman-contribution-graph.git temp_pacman

# 3. Customização
python3 scripts/custom_pacman_generator.py halloween
# Modifica: temp_pacman/src/core/constants.ts

# 4. Build
cd temp_pacman && npm install && npm run build
cd github-action && npm install && npm run build

# 5. Geração
cd github-action && node dist/index.js
# Cria: dist/pacman-contribution-graph.svg (com cores laranja/roxo!)

# 6. Deploy
# SVG vai para branch 'output' automaticamente
```

### Output
- ✅ Pacman com cores **laranja e roxo** de Halloween
- ✅ Visível no README.md do perfil
- ✅ Atualizado a cada 12 horas

## 📅 Calendário Automático

O sistema muda as cores automaticamente baseado na data:

| Data | Tema | Cores Aplicadas |
|------|------|-----------------|
| **31/10** | 🎃 **Halloween** | **Laranja + Roxo** |
| 24-25/12 | 🎄 Natal | Azul Frio |
| 31/12-01/01 | 🎊 Ano Novo | Rosa Neon |
| 07/09 | 🇧🇷 Independência | Verde + Amarelo |
| 13/09 | 💻 Programador | Synthwave |
| ... | ... | ... |

**Totalmente automático!** Não precisa fazer nada.

## ⚙️ Configurações do Workflow

### Triggers

```yaml
on:
  schedule:
    - cron: "* */12 * * *"  # A cada 12 horas
  
  workflow_dispatch:  # Manual (Actions > Run workflow)
  
  push:
    branches:
    - main  # Cada push na main
```

### Variáveis de Ambiente

Todas configuradas automaticamente:

```yaml
GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # Auto-gerado
GITHUB_REPOSITORY_OWNER: ${{ github.repository_owner }}  # Seu user
INPUT_GITHUB_USER_NAME: ${{ github.repository_owner }}  # Para a action
```

### Timeout

```yaml
timeout-minutes: 10  # Máximo 10 minutos
```

## 📊 Exemplo de Execução

### Log no GitHub Actions

```
🎨 Detectando tema atual...
✅ Tema detectado: halloween
📝 🎃 Tema de Halloween - Laranja e Roxo Assustador

📦 Clonando repositório do Pacman...
Cloning into 'temp_pacman'...
✅ Tema aplicado com sucesso!

📦 Instalando dependências...
✅ Build concluído!

📦 Instalando dependências da action...
✅ Action pronta!

🎮 Gerando Pacman com tema: halloween
📝 🎃 Tema de Halloween - Laranja e Roxo Assustador
👤 Usuário: goul4rt

💾 writing to dist/pacman-contribution-graph.svg
💾 writing to dist/pacman-contribution-graph-dark.svg

✅ SVG light copiado
✅ SVG dark copiado

═══════════════════════════════════════════════
🎉 PACMAN GERADO COM SUCESSO!
═══════════════════════════════════════════════
🎨 Tema: halloween
📝 🎃 Tema de Halloween - Laranja e Roxo Assustador
📅 Data: 31/10/2025
═══════════════════════════════════════════════

🧹 Limpeza concluída
```

## 🎯 Resultado Final

### No seu README.md

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" 
          srcset="https://raw.githubusercontent.com/goul4rt/goul4rt/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" 
          srcset="https://raw.githubusercontent.com/goul4rt/goul4rt/output/pacman-contribution-graph.svg">
  <img alt="pacman contribution graph" 
       src="https://raw.githubusercontent.com/goul4rt/goul4rt/output/pacman-contribution-graph.svg">
</picture>
```

### Cores Aplicadas (Halloween)

```css
Background:    #1a1423  /* Roxo escuro assustador */
Paredes:       #ff6b35  /* Laranja vibrante */
Pac-Man:       #ffa500  /* Laranja brilhante */
Contribuições:
  - Nenhuma:   #2d1b2e  /* Muito escuro */
  - Poucas:    #5c3d5e  /* Roxo escuro */
  - Moderadas: #9b4f8e  /* Roxo médio */
  - Muitas:    #ff6b35  /* Laranja */
  - Máximas:   #ffa500  /* Laranja brilhante */
```

## 🔍 Verificação

### Como verificar se está funcionando:

1. **Vá para Actions no GitHub**
   - https://github.com/SEU_USUARIO/SEU_REPO/actions

2. **Veja o workflow "Generate pacman animation"**
   - Deve estar verde ✅

3. **Veja os logs**
   - Clique no workflow > Expand steps
   - Deve mostrar tema detectado e cores aplicadas

4. **Veja o SVG gerado**
   - https://raw.githubusercontent.com/SEU_USUARIO/SEU_USUARIO/output/pacman-contribution-graph.svg
   - Deve ter as cores do tema atual

5. **Veja no README**
   - https://github.com/SEU_USUARIO
   - Pacman deve estar com cores do tema

## 🐛 Troubleshooting

### Workflow falha no build

**Causa**: Dependências não instaladas ou erro no npm

**Solução**: O workflow tem `continue-on-error: true`, então não quebra

### SVG não é gerado

**Causa**: Token do GitHub pode estar inválido

**Solução**: GitHub Actions usa token automático, não precisa configurar

### Tema não muda

**Causa**: Pode estar usando cache antigo

**Solução**: 
1. Vá em Actions
2. Clique em "Run workflow"
3. Selecione "Run workflow" novamente

### SVG tem cores erradas

**Causa**: Tema pode não ter sido aplicado

**Solução**: Veja os logs do step "Clone and customize Pacman"

## 📝 Notas Importantes

### 1. Primeira Execução

Na primeira vez pode demorar mais (~5-8 minutos):
- Clone do repositório
- npm install (muitas dependências)
- Build completo

### 2. Execuções Seguintes

Depois é mais rápido (~3-5 minutos):
- GitHub Actions tem cache
- Build é incremental

### 3. Rate Limits

GitHub tem limites de API:
- Workflow roda a cada 12 horas
- Isso evita rate limits
- Se precisar manual: workflow_dispatch

### 4. Branch Output

Os SVGs vão para branch `output`:
- Branch criada automaticamente
- Não precisa criar manualmente
- GitHub Pages pode usar

## 🎉 Conclusão

**Sistema 100% Automático!**

- ✅ Zero configuração manual
- ✅ Zero manutenção
- ✅ Mudanças automáticas de tema
- ✅ Sincronizado com celebration_generator.py
- ✅ Logs completos e informativos
- ✅ Cleanup automático
- ✅ Fallbacks para erros

**Você não precisa fazer NADA!**

O sistema:
1. Detecta a data
2. Escolhe o tema
3. Clona o código
4. Aplica as cores
5. Builda tudo
6. Gera o SVG
7. Faz deploy
8. Limpa tudo

Completamente automático! 🚀

---

**Happy Halloween! 🎃**

*Última atualização: 31 de Outubro de 2025*

