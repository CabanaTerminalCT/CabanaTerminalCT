# =============================================================================
# 082 - Importa funcao
# Nivel: 2 estrelas
# Conceitos: from x import y
# =============================================================================
#
# HISTORIA
# --------
# As vezes escrever math.sqrt toda hora enche. Com "from math import sqrt" voce
# traz so o que precisa, direto. A CabanaTerminal usa os dois estilos conforme
# a situacao.
#
# TAREFA
# ------
# 1. Use "from math import sqrt, pow" e calcule sqrt(81) e pow(2, 10)
# 2. Use "from random import randint" e sorteie um numero de 1 a 6 (dado)
# 3. Comente a diferenca entre importar o modulo todo e importar so a funcao
#
# Exemplo de execucao:
#
#   $ python3 082_importa_funcao.py
#   Raiz de 81: 9.0
#   2 elevado a 10: 1024.0
#   Dado: 4
#
# REQUISITOS
# ----------
# [ ] Usa "from x import y"
# [ ] Chama a funcao sem o prefixo do modulo
# [ ] Importa de pelo menos dois modulos
#
# DICA
# ----
# "from math import sqrt" permite chamar sqrt(81) direto. Cuidado com nomes
# genericos - importar tudo com "*" pode sobrescrever funcoes suas.
#
# VALIDACAO
# ---------
# sqrt(81) -> 9.0; pow(2,10) -> 1024.0; o dado sai entre 1 e 6.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
