# 🎮 Pacman Contribution Graph - Customização de Cores

> Sistema para customizar as cores do Pacman Contribution Graph baseado em celebrações

## 📚 Documentação

- **[QUICK_START.md](./QUICK_START.md)** - Comece aqui! Guia rápido (5 min)
- **[PACMAN_CUSTOMIZATION.md](./PACMAN_CUSTOMIZATION.md)** - Documentação completa e detalhada
- **[SUMMARY.md](./SUMMARY.md)** - Resumo do que foi criado

## 🚀 Início Rápido

```bash
# Ver tema atual (detectado automaticamente pela data)
python3 scripts/pacman_theme_generator.py

# Ver todos os 17 temas disponíveis
python3 scripts/pacman_theme_generator.py --list

# Aplicar tema atual no código do Pacman
python3 scripts/custom_pacman_generator.py

# Aplicar um tema específico
python3 scripts/custom_pacman_generator.py halloween
```

## 🎨 Temas Disponíveis (17)

| Tema | Data | Cores |
|------|------|-------|
| 🎃 Halloween | 31/10 | Laranja + Roxo |
| 🎄 Natal | 24-25/12 | Azul Frio |
| 🎊 Ano Novo | 31/12-01/01 | Rosa Neon |
| 💻 Programador | 13/09 | Synthwave |
| 🇧🇷 Independência | 07/09 | Verde + Amarelo |
| 🎭 Carnaval | 12-14/02 | Vibrante |
| 🌽 São João | 23-24/06 | Quente |
| ⚔️ Star Wars | 04/05 | Roxo + Verde |
| 🥧 Pi Day | 14/03 | Azul |
| 👩‍💻 Grace Hopper | 09/12 | OneDark |
| 🎮 Video Game | 29/08 | Dracula |
| 💘 Valentine's | 14/02 | Rosa |
| 🤡 April Fools | 01/04 | Maluco |
| 🔭 Towel Day | 25/05 | Cobalt |
| ⚡ Back to Future | 21/10 | Synthwave |
| 🌍 Earth Day | 22/04 | Verde |
| 🌙 Default | Outros | Tokyo Night |

## 📁 Estrutura de Arquivos

```
scripts/
├── README_PACMAN.md                   # Este arquivo
├── QUICK_START.md                     # Guia rápido
├── PACMAN_CUSTOMIZATION.md            # Docs completa
├── SUMMARY.md                         # Resumo do projeto
│
├── pacman_theme_generator.py          # Gerador de temas
├── custom_pacman_generator.py         # Aplicador de temas
│
├── pacman_theme.json                  # Tema atual gerado
├── current_pacman_theme.json          # Info de aplicação
│
└── pacman_theme_previews/             # Previews dos temas
    ├── theme_halloween.json
    ├── theme_natal.json
    └── ... (17 temas)
```

## 🎃 Tema Atual

**Hoje é 31 de Outubro - Halloween!**

O tema Halloween está ativo com:
- Background roxo escuro (`#1a1423`)
- Paredes laranjas (`#ff6b35`)
- Pac-Man laranja brilhante (`#ffa500`)
- Gradiente de intensidade roxo → laranja

```bash
# Ver tema atual
cat scripts/pacman_theme.json
```

## 💡 Como Funciona

1. **Detecção**: Script detecta a data atual
2. **Seleção**: Escolhe o tema correspondente
3. **Geração**: Cria JSON com cores
4. **Aplicação**: Modifica `constants.ts` do Pacman
5. **Build**: (Opcional) Gera SVG customizado

## 🔗 Integração

Este sistema se integra com:
- ✅ `celebration_generator.py` - Mesmas datas
- ✅ Workflow GitHub Actions
- ✅ Pacman original (fork ou local)

## 📊 O que foi Criado

- ✅ 17 temas com cores harmoniosas
- ✅ Sistema de detecção automática
- ✅ Scripts Python documentados
- ✅ Previews de todos os temas
- ✅ Documentação completa
- ✅ Código do Pacman modificado

## 🎯 Status

**✅ 100% COMPLETO E FUNCIONAL**

Todos os TODOs foram concluídos:
- [x] Temas criados
- [x] Gerador implementado
- [x] Aplicador funcionando
- [x] Documentação completa
- [x] Testes realizados

## 🚀 Próximos Passos

1. **Testar localmente** (opcional)
   ```bash
   cd temp_pacman_source
   npm install && npm run build
   ```

2. **Fork do repositório** (para usar no GitHub)
   - Fork de `abozanona/pacman-contribution-graph`
   - Aplicar seus temas
   - Usar no workflow

3. **Adicionar novos temas**
   - Editar `pacman_theme_generator.py`
   - Definir cores e datas
   - Aplicar com `custom_pacman_generator.py`

## 🎨 Exemplo de Customização

```python
# Adicionar novo tema em pacman_theme_generator.py

PACMAN_THEMES = {
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
    'meu_tema': [(3, 15)]  # 15 de março
}
```

## 📞 Suporte

Se algo não funcionar:

1. Verifique se o `temp_pacman_source/` existe
2. Execute `python3 scripts/pacman_theme_generator.py --list`
3. Veja os logs em `scripts/current_pacman_theme.json`
4. Leia a documentação completa em `PACMAN_CUSTOMIZATION.md`

## 🎉 Créditos

- **Código Original**: [abozanona/pacman-contribution-graph](https://github.com/abozanona/pacman-contribution-graph)
- **Sistema de Celebrações**: celebration_generator.py
- **Customização**: Este sistema de temas

---

**Happy Coding! 🎮✨**

*Última atualização: 31 de Outubro de 2025 - Halloween* 🎃

