# 🔄 Integração com Workflow - Pacman Customizado

## 📋 Visão Geral

Este guia mostra como integrar o Pacman customizado com seu GitHub Actions workflow.

## 🎯 Objetivo

Fazer o Pacman do seu perfil mudar de cor automaticamente baseado na data, assim como o README já muda com o `celebration_generator.py`.

## 🛠️ Opções de Integração

### Opção 1: Fork do Repositório (Recomendado) ⭐

Esta é a melhor opção para ter controle total.

#### Passos:

1. **Fork do repositório original**
   ```bash
   # Vá para: https://github.com/abozanona/pacman-contribution-graph
   # Clique em "Fork"
   ```

2. **Clone seu fork**
   ```bash
   git clone https://github.com/SEU_USUARIO/pacman-contribution-graph.git my-pacman
   cd my-pacman
   ```

3. **Copie os temas modificados**
   ```bash
   # Do seu workspace:
   cp temp_pacman_source/src/core/constants.ts my-pacman/src/core/constants.ts
   ```

4. **Commit e push**
   ```bash
   cd my-pacman
   git add src/core/constants.ts
   git commit -m "feat: add custom celebration themes"
   git push origin main
   ```

5. **Atualize seu workflow**
   ```yaml
   # .github/workflows/packman.yml
   - name: generate pacman-contribution-graph.svg
     uses: SEU_USUARIO/pacman-contribution-graph@main
     with:
       github_user_name: ${{ github.repository_owner }}
   ```

#### Vantagens:
- ✅ Controle total sobre o código
- ✅ Pode fazer releases próprias
- ✅ Funciona como GitHub Action nativa
- ✅ Fácil de manter

#### Desvantagens:
- ⏰ Precisa manter fork atualizado com upstream
- 🔄 Mudanças exigem novo commit

---

### Opção 2: Action Local 📁

Use o código buildado localmente no seu repositório.

#### Passos:

1. **Build do código**
   ```bash
   cd temp_pacman_source
   npm install
   npm run build
   
   cd github-action
   npm install
   npm run build
   ```

2. **Copie para seu repositório**
   ```bash
   mkdir -p .github/actions/pacman-custom
   cp -r temp_pacman_source/github-action/dist .github/actions/pacman-custom/
   cp temp_pacman_source/github-action/action.yml .github/actions/pacman-custom/
   cp -r temp_pacman_source/dist .github/actions/pacman-custom/lib
   ```

3. **Crie action.yml customizado**
   ```yaml
   # .github/actions/pacman-custom/action.yml
   name: 'Pacman Custom'
   description: 'Generates Pacman with custom themes'
   
   inputs:
     github_user_name:
       description: 'GitHub username'
       required: true
     github_token:
       description: 'GitHub token'
       required: false
       default: ${{ github.token }}
   
   runs:
     using: 'node20'
     main: 'dist/index.js'
   ```

4. **Atualize workflow**
   ```yaml
   # .github/workflows/packman.yml
   - name: Checkout
     uses: actions/checkout@v3
   
   - name: Generate custom pacman
     uses: ./.github/actions/pacman-custom
     with:
       github_user_name: ${{ github.repository_owner }}
   ```

#### Vantagens:
- ✅ Não precisa de fork
- ✅ Tudo no mesmo repositório
- ✅ Rápido de implementar

#### Desvantagens:
- ❌ Código buildado (binário) no git
- ❌ Dificulta code review
- ❌ Aumenta tamanho do repo

---

### Opção 3: Script Python + CLI 🐍

Use a CLI do pacman com Python para gerar temas dinamicamente.

#### Passos:

1. **Crie script de integração**
   ```python
   # .github/scripts/generate_pacman.py
   import subprocess
   import json
   from pathlib import Path
   import sys
   
   # Importa o gerador de temas
   sys.path.append('scripts')
   from pacman_theme_generator import get_current_celebration_theme
   
   def main():
       # Detecta tema atual
       celebration, theme = get_current_celebration_theme()
       
       print(f"🎨 Usando tema: {celebration}")
       print(f"📝 {theme['description']}")
       
       # Instala pacman CLI
       subprocess.run(['npm', 'install', '-g', 'pacman-contribution-graph'], check=True)
       
       # Gera SVGs (infelizmente a CLI não aceita temas customizados ainda)
       # Você precisaria modificar a biblioteca ou usar Opção 1/2
       
       print("⚠️  A CLI do Pacman não suporta temas customizados.")
       print("💡 Use Opção 1 (Fork) ou Opção 2 (Action Local)")
   
   if __name__ == '__main__':
       main()
   ```

2. **Workflow**
   ```yaml
   - name: Setup Python
     uses: actions/setup-python@v4
     with:
       python-version: '3.x'
   
   - name: Generate Pacman
     run: python3 .github/scripts/generate_pacman.py
   ```

#### Vantagens:
- ✅ Detecção automática de tema
- ✅ Integra com celebration_generator.py

#### Desvantagens:
- ❌ CLI não suporta temas customizados nativamente
- ❌ Precisaria modificar biblioteca de qualquer forma

---

## 🎨 Workflow Completo Recomendado

Combina celebrações do README com Pacman customizado:

```yaml
name: Update Profile

on:
  schedule:
    - cron: "0 0 * * *"  # Todo dia à meia-noite
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    
    steps:
      # 1. Checkout
      - name: Checkout
        uses: actions/checkout@v3
      
      # 2. Setup Python para celebrações
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      # 3. Gera README com tema
      - name: Generate celebration README
        run: python3 scripts/celebration_generator.py
      
      # 4. Detecta tema atual
      - name: Detect current theme
        id: theme
        run: |
          THEME=$(python3 scripts/pacman_theme_generator.py | grep "Tema gerado:" | cut -d':' -f2 | tr -d ' ')
          echo "current_theme=$THEME" >> $GITHUB_OUTPUT
          echo "🎨 Tema detectado: $THEME"
      
      # 5. Gera Pacman customizado
      - name: Generate custom Pacman
        uses: SEU_USUARIO/pacman-contribution-graph@main
        # OU
        # uses: ./.github/actions/pacman-custom
        with:
          github_user_name: ${{ github.repository_owner }}
      
      # 6. Commit mudanças
      - name: Commit changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git diff --quiet && git diff --staged --quiet || \
            git commit -m "🎨 Update profile with theme: ${{ steps.theme.outputs.current_theme }}"
      
      # 7. Push SVGs para branch output
      - name: Push Pacman SVGs
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 🔄 Atualização Dinâmica

Para mudar o tema do Pacman dinamicamente no workflow:

### Modificação do index.js da Action

```javascript
// github-action/src/index.js
import * as core from '@actions/core';
import { execSync } from 'child_process';

// Detecta tema atual via Python
const detectTheme = () => {
    try {
        const result = execSync('python3 scripts/pacman_theme_generator.py', {
            encoding: 'utf-8'
        });
        
        // Parse do tema
        const themeMatch = result.match(/Tema gerado: (\w+)/);
        return themeMatch ? themeMatch[1] : 'default';
    } catch (error) {
        console.log('❌ Erro ao detectar tema, usando default');
        return 'default';
    }
};

const generateSvg = async (userName, githubToken, playerStyle) => {
    const theme = detectTheme();
    console.log(`🎨 Usando tema: ${theme}`);
    
    return new Promise((resolve, reject) => {
        // ... resto do código com tema dinâmico
        const conf = {
            platform: "github",
            username: userName,
            outputFormat: "svg",
            gameSpeed: 1,
            gameTheme: theme,  // Tema dinâmico!
            // ...
        };
    });
};
```

## 📊 Exemplo de Resultado

### Antes (Original)
```
README.md (normal)
+ Pacman verde padrão
```

### Depois (Com Sistema)

#### No Halloween (31/10):
```
README.md (tema Halloween 🎃)
+ Pacman laranja/roxo assustador 🎃
```

#### No Natal (24-25/12):
```
README.md (tema Natal 🎄)
+ Pacman azul frio nórdico ❄️
```

#### Em dias normais:
```
README.md (sem tema especial)
+ Pacman Tokyo Night padrão 🌙
```

## 🎯 Próximos Passos

Escolha sua opção de integração:

1. **Para produção**: Use **Opção 1** (Fork)
   - Mais profissional
   - Fácil de manter
   - Funciona perfeitamente

2. **Para teste rápido**: Use **Opção 2** (Local)
   - Rápido de implementar
   - Testa sem fazer fork

3. **Para futuro**: Contribua com o projeto original
   - Faça PR com suporte a temas customizados
   - Beneficia toda a comunidade

## 💡 Dicas

### Sincronização de Temas
```bash
# Sempre use as mesmas datas em ambos os arquivos
celebration_generator.py  # 'halloween': [(10, 31)]
pacman_theme_generator.py # 'halloween': [(10, 31)]
```

### Cache do Workflow
```yaml
- name: Cache npm
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

### Debug de Temas
```yaml
- name: Debug theme
  run: |
    python3 scripts/pacman_theme_generator.py
    cat scripts/pacman_theme.json
    cat scripts/current_pacman_theme.json
```

## 🐛 Troubleshooting

### Tema não muda
```bash
# Verifique se o tema foi aplicado
cat temp_pacman_source/src/core/constants.ts | grep halloween

# Verifique a data
python3 -c "from datetime import datetime; print((datetime.now().month, datetime.now().day))"

# Teste manualmente
python3 scripts/pacman_theme_generator.py
```

### Build falha
```bash
# Limpe e reinstale
rm -rf temp_pacman_source/node_modules
cd temp_pacman_source
npm install
npm run build
```

### Fork desatualizado
```bash
# Adicione upstream
git remote add upstream https://github.com/abozanona/pacman-contribution-graph.git

# Atualize
git fetch upstream
git merge upstream/main

# Reaplique temas
python3 scripts/custom_pacman_generator.py
```

## 📚 Referências

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Pacman Original](https://github.com/abozanona/pacman-contribution-graph)
- [Custom Actions](https://docs.github.com/en/actions/creating-actions)

---

## 🎉 Conclusão

Você tem **3 opções** para integrar:

| Opção | Dificuldade | Recomendado | Manutenção |
|-------|------------|-------------|------------|
| 1. Fork | Média | ⭐⭐⭐⭐⭐ | Fácil |
| 2. Local | Fácil | ⭐⭐⭐ | Média |
| 3. CLI | Difícil | ⭐ | Complexa |

**Recomendação: Use Opção 1 (Fork)** 🎯

---

**Boa sorte com a integração! 🚀**

*Happy Halloween! 🎃*

