# =============================================================================
# 076 - Escreve CSV
# Nivel: 4 estrelas
# Conceitos: modulo csv
# =============================================================================
#
# HISTORIA
# --------
# Depois do mutirao a CabanaTerminal precisa exportar o placar pra planilha.
# csv.writer grava as linhas ja no formato certo, com as virgulas no lugar.
#
# TAREFA
# ------
# 1. Monte uma lista de membros com nome e pontos
# 2. Abra "placar.csv" em modo escrita
# 3. Use csv.writer pra gravar o cabecalho e as linhas
# 4. Leia de volta e confirme
#
# Exemplo de execucao:
#
#   $ python3 076_escreve_csv.py
#   Gravado placar.csv
#   Conteudo:
#   nome,pontos
#   ana,10
#   bruno,20
#
# REQUISITOS
# ----------
# [ ] Importa csv
# [ ] Usa csv.writer
# [ ] Grava cabecalho e pelo menos 2 linhas
# [ ] Le de volta pra validar
#
# DICA
# ----
# writer.writerow(lista) grava uma linha. Passe newline="" no open pra evitar
# linhas em branco extras no Windows.
#
# VALIDACAO
# ---------
# O arquivo placar.csv contem o cabecalho e as linhas, sem linhas vazias
# sobrando.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
