# =============================================================================
# 017 - Fuga do loop
# Nivel: 3 estrelas
# Conceitos: break
# =============================================================================
#
# HISTORIA
# --------
# Tem um numero secreto guardado no cofre da CabanaTerminal. O programa fica
# pedindo palpites num loop, mas quando alguem acerta, o loop para na hora
# com break. Nada de continuar rodando depois do gol.
#
# TAREFA
# ------
# 1. Defina um numero secreto (ex: 42)
# 2. Fique pedindo palpites num while
# 3. Quando acertar, imprima "Acertou!" e saia do loop com break
# 4. Se errar, avise se o palpite foi maior ou menor
#
# Exemplo de execucao:
#
#   $ python3 017_fuga_do_loop.py
#   Palpite: 10
#   Muito baixo!
#   Palpite: 50
#   Muito alto!
#   Palpite: 42
#   Acertou! O numero secreto era 42.
#
# REQUISITOS
# ----------
# [ ] Usa while True (loop aparentemente infinito)
# [ ] Usa break pra sair quando acertar
# [ ] Da a dica "muito alto" / "muito baixo"
#
# DICA
# ----
# while True roda pra sempre - quem controla a saida e o break:
#
#   while True:
#       palpite = int(input("Palpite: "))
#       if palpite == secreto:
#           print("Acertou!")
#           break
#
# VALIDACAO
# ---------
# Erre algumas vezes e acerte no fim. O programa encerra assim que acertar.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
