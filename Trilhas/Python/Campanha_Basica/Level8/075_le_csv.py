# =============================================================================
# 075 - Le CSV
# Nivel: 4 estrelas
# Conceitos: modulo csv
# =============================================================================
#
# HISTORIA
# --------
# A planilha de pontos da CabanaTerminal veio em CSV - valores separados por
# virgula. O modulo csv do Python le isso direitinho, cuidando das virgulas
# dentro dos campos pra voce.
#
# TAREFA
# ------
# 1. Crie um arquivo "pontos.csv" com um cabecalho e algumas linhas
#    (ex: nome,pontos)
# 2. Leia com csv.reader
# 3. Imprima cada linha
# 4. Some a coluna de pontos e mostre o total
#
# Exemplo de execucao:
#
#   $ python3 075_le_csv.py
#   ['nome', 'pontos']
#   ['ana', '10']
#   ['bruno', '20']
#   ['carla', '15']
#   Total de pontos: 45
#
# REQUISITOS
# ----------
# [ ] Importa o modulo csv
# [ ] Usa csv.reader
# [ ] Pula o cabecalho ao somar
# [ ] Converte os valores com int()
#
# DICA
# ----
# csv.reader devolve cada linha como lista de strings. Pule o cabecalho com
# next(leitor) ou um slice [1:]. Converta com int(linha[1]).
#
# VALIDACAO
# ---------
# Com 10, 20 e 15 -> total 45.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
