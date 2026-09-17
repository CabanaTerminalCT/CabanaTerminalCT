# =============================================================================
# 064 - Senao deu certo
# Nivel: 3 estrelas
# Conceitos: else do try
# =============================================================================
#
# HISTORIA
# --------
# O else do try roda so quando NENHUM erro aconteceu. Serve pra separar o
# codigo que pode falhar do codigo que so faz sentido se deu tudo certo - o
# terminal da CabanaTerminal fica mais claro assim.
#
# TAREFA
# ------
# 1. Peca um numero
# 2. No try, converta pra inteiro
# 3. No except, avise do erro
# 4. No else, so rode se a conversao deu certo: mostre o dobro do numero
#
# Exemplo de execucao:
#
#   $ python3 064_senao_deu_certo.py
#   Numero: 7
#   Tudo certo! O dobro e 14.
#
#   $ python3 064_senao_deu_certo.py
#   Numero: x
#   Deu erro na conversao.
#
# REQUISITOS
# ----------
# [ ] Usa try/except/else
# [ ] O calculo do dobro fica no else (nao no try)
# [ ] So imprime o dobro quando nao houve erro
#
# DICA
# ----
# Estrutura: try -> except -> else. O else nunca roda se o except rodar, e
# vice-versa. Deixe no try apenas o que pode lancar a excecao.
#
# VALIDACAO
# ---------
# "7" -> dobro 14; "x" -> mensagem de erro, sem imprimir dobro.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
