# =============================================================================
# 061 - Erro e normal
# Nivel: 2 estrelas
# Conceitos: try/except
# =============================================================================
#
# HISTORIA
# --------
# Na CabanaTerminal erro nao e vergonha, e informacao. Em vez de deixar o
# programa morrer, a gente envolve o trecho arriscado num try e trata o
# problema no except.
#
# TAREFA
# ------
# 1. Peca um numero ao usuario
# 2. Converta pra inteiro dentro de um try
# 3. Se der erro, o except avisa que a entrada nao e valida
# 4. Mostre uma mensagem de sucesso se der tudo certo
#
# Exemplo de execucao:
#
#   $ python3 061_erro_e_normal.py
#   Numero: 10
#   Voce digitou 10
#
#   $ python3 061_erro_e_normal.py
#   Numero: abc
#   Isso nao e um numero valido.
#
# REQUISITOS
# ----------
# [ ] Usa try
# [ ] Usa except
# [ ] O programa nao quebra com entrada invalida
#
# DICA
# ----
# Coloque dentro do try so o que pode dar erro:
#
#   try:
#       n = int(input("Numero: "))
#       print(f"Voce digitou {n}")
#   except:
#       print("Isso nao e um numero valido.")
#
# VALIDACAO
# ---------
# Com "10" funciona; com "abc" mostra o aviso e o programa segue vivo.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
