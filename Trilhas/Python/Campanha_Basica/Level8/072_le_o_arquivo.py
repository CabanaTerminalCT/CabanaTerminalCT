# =============================================================================
# 072 - Le o arquivo
# Nivel: 3 estrelas
# Conceitos: read(), readlines()
# =============================================================================
#
# HISTORIA
# --------
# Gravar sem conseguir ler nao serve pra nada. A CabanaTerminal agora abre o
# arquivo que voce escreveu e mostra o conteudo - inteiro ou linha por linha.
#
# TAREFA
# ------
# 1. Crie um arquivo "notas.txt" com 3 linhas (pode ser pelo editor ou pelo
#    desafio anterior)
# 2. Abra em modo leitura ("r")
# 3. Leia o conteudo inteiro com .read() e mostre
# 4. Reabra e leia linha por linha com .readlines(), imprimindo numerado
#
# Exemplo de execucao:
#
#   $ python3 072_le_o_arquivo.py
#   --- conteudo completo ---
#   linha um
#   linha dois
#   linha tres
#   --- linha por linha ---
#   1: linha um
#   2: linha dois
#   3: linha tres
#
# REQUISITOS
# ----------
# [ ] Usa open() modo "r"
# [ ] Usa .read()
# [ ] Usa .readlines() e percorre
#
# DICA
# ----
# .read() devolve tudo numa string. .readlines() devolve uma lista de linhas
# (cada uma termina com "\n"). Use .strip() pra limpar.
#
# VALIDACAO
# ---------
# O conteudo aparece completo e depois numerado linha a linha.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
