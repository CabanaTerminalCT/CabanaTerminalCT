# =============================================================================
# 040 - Mini-projeto: controle de gastos
# Nivel: 4 estrelas
# Conceitos: listas (append, sum, max, min, for)
# =============================================================================
#
# HISTORIA
# --------
# O caixa da CabanaTerminal precisa de controle. Voce vai fazer um pequeno
# sistema que registra gastos num loop e, no fim, mostra o resumo financeiro.
# Junta tudo do capitulo de listas num programa so.
#
# TAREFA
# ------
# 1. Fique pedindo valores de gasto ate o usuario digitar "sair"
# 2. Guarde cada gasto numa lista
# 3. No fim, mostre:
#      - todos os gastos
#      - total gasto
#      - maior gasto
#      - menor gasto
#      - media dos gastos
#      - quantidade de gastos
#
# Exemplo de execucao:
#
#   $ python3 040_controle_de_gastos.py
#   Gasto (ou 'sair'): 100
#   Gasto (ou 'sair'): 50
#   Gasto (ou 'sair'): 75
#   Gasto (ou 'sair'): sair
#
#   === RESUMO ===
#   Gastos: [100.0, 50.0, 75.0]
#   Total: 225.0
#   Maior: 100.0
#   Menor: 50.0
#   Media: 75.0
#   Quantidade: 3
#
# REQUISITOS
# ----------
# [ ] Usa while pra ler ate "sair"
# [ ] Converte com float() e adiciona com .append()
# [ ] Usa sum(), max(), min(), len()
# [ ] Trata o caso de lista vazia (nao quebrar sem nenhum gasto)
#
# DICAS
# -----
# - Leia o input como texto, cheque "sair" ANTES de converter pra float.
# - Se a lista estiver vazia no final, avise "nenhum gasto registrado" em vez
#   de dividir por zero.
#
# VALIDACAO
# ---------
# Com 100, 50, 75 -> total 225, maior 100, menor 50, media 75, quantidade 3.
# Sem nenhum gasto -> mensagem amigavel, sem erro.
#
# Terminou? Voce fechou o Capitulo 4. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
