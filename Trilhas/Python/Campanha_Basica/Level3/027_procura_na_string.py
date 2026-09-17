# =============================================================================
# 027 - Procura na string
# Nivel: 3 estrelas
# Conceitos: in, .find(), .count()
# =============================================================================
#
# HISTORIA
# --------
# O moderador da CabanaTerminal precisa achar palavras proibidas no chat.
# Procurar dentro de texto e tarefa de todo dia: vale pra busca, validacao e
# filtro.
#
# TAREFA
# ------
# 1. Peca uma frase ao usuario
# 2. Peca uma palavra pra procurar
# 3. Diga se a palavra esta na frase (use "in")
# 4. Mostre a posicao da primeira ocorrencia (.find())
# 5. Mostre quantas vezes ela aparece (.count())
#
# Exemplo de execucao:
#
#   $ python3 027_procura_na_string.py
#   Frase: cabana cabana cabana
#   Procurar: cabana
#   Esta na frase? True
#   Primeira posicao: 0
#   Ocorrencias: 3
#
# REQUISITOS
# ----------
# [ ] Usa "in" retornando bool
# [ ] Usa .find()
# [ ] Usa .count()
#
# DICA
# ----
# .find() devolve -1 quando nao acha; "in" devolve True/False. .count() devolve
# 0 quando nao acha.
#
# VALIDACAO
# ---------
# "cabana cabana cabana" + "cabana" -> True, 0, 3.
# Palavra inexistente -> False, -1, 0.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
