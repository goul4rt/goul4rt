# 🎉 Sistema de Decorações Comemorativas

Este sistema atualiza automaticamente o README do perfil com decorações temáticas em datas especiais!

## 🚀 Como Funciona

1. **Workflow Automático**: Roda diariamente à meia-noite (UTC) verificando se é uma data especial
2. **Script Python**: Detecta a data atual e aplica a decoração correspondente
3. **Commit Automático**: Se houver mudanças, o bot faz commit automaticamente

## 📅 Datas Comemorativas Configuradas

| Data | Celebração | Tema |
|------|-----------|------|
| 31/10 | 🎃 Halloween | halloween |
| 24-25/12 | 🎄 Natal | nord |
| 31/12 - 01/01 | 🎊 Ano Novo | radical |
| 07/09 | 🇧🇷 Independência do Brasil | chartreuse-dark |
| 13/09 | 💻 Dia do Programador | synthwave |
| 12-14/02 | 🎭 Carnaval | radical |

## ➕ Como Adicionar Novas Datas

Edite o arquivo `scripts/celebration_generator.py` e adicione uma nova entrada no dicionário `CELEBRATIONS`:

```python
'nome_celebracao': {
    'dates': [(mes, dia)],  # Lista de tuplas (mês, dia)
    'header': '🎉 <h3 align="center">Título da Celebração! 🎊</h3>\n...',
    'theme': 'nome_do_tema',  # Temas disponíveis no GitHub Stats
    'gif_url': 'https://media.giphy.com/...',  # URL do GIF temático
    'footer': '\n\n<div align="center">\n  <h3>Mensagem!</h3>\n</div>\n'
}
```

### 🎨 Temas Disponíveis

Alguns temas populares do GitHub Stats:
- `tokyonight` (padrão)
- `halloween` (laranja/roxo)
- `nord` (azul frio)
- `radical` (rosa/roxo)
- `synthwave` (neon)
- `chartreuse-dark` (verde/escuro)
- `dracula` (roxo escuro)
- `monokai` (amarelo/verde)

Veja mais em: [github-readme-stats themes](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md)

### 🖼️ Encontrar GIFs

Use o [GIPHY](https://giphy.com/) para encontrar GIFs temáticos. Copie o link direto do GIF.

## 🧪 Testar Localmente

```bash
# Testar o script
python3 scripts/celebration_generator.py

# Ver o README gerado
cat README.md
```

## ⚙️ Executar Manualmente

Se quiser forçar uma atualização sem esperar o cron job:

1. Acesse: `Actions` no GitHub
2. Selecione: `Update Profile with Celebrations`
3. Clique: `Run workflow` → `Run workflow`

## 📝 Notas

- O script preserva todo o conteúdo original do README
- Apenas muda o header, tema dos stats, GIF e adiciona um footer
- Quando não há celebração, volta ao tema padrão
- O workflow não faz commit se não houver mudanças

## 🔧 Estrutura de Arquivos

```
.github/workflows/
  └── celebration.yml          # Workflow de atualização automática
scripts/
  ├── celebration_generator.py # Script principal
  └── README.md               # Esta documentação
README.md                     # Perfil do GitHub (gerado)
```

## 🎯 Próximos Passos

Ideias para melhorar:
- [ ] Adicionar suporte para Páscoa (data móvel)
- [ ] Criar temas personalizados
- [ ] Adicionar mais GIFs e animações
- [ ] Suporte para múltiplas línguas
- [ ] Decorações por estação do ano
- [ ] Badges especiais para cada celebração

