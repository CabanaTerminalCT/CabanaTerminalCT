# =============================================================================
# 016 - Caca-vogais
# Nivel: 3 estrelas
# Conceitos: for + string
# =============================================================================
#
# HISTORIA
# --------
# Alguem colou um codigo cheio de vogais no chat da CabanaTerminal e voce
# decidiu contar quantas tem. Percorrer uma string caractere por caractere e
# uma das coisas mais uteis que um loop faz.
#
# TAREFA
# ------
# 1. Peca uma palavra ao usuario
# 2. Conte quantas vogais (a, e, i, o, u) ela tem
# 3. Mostre a quantidade
#
# Exemplo de execucao:
#
#   $ python3 016_caca_vogais.py
#   Palavra: cabana
#   Vogais: 3
#
# REQUISITOS
# ----------
# [ ] Usa for pra percorrer a string
# [ ] Conta apenas a, e, i, o, u
# [ ] Mostra o total
#
# DICA
# ----
# Voce pode percorrer a string direto: "for letra in palavra".
# Pra checar se a letra esta entre as vogais use "in":
#
#   if letra in "aeiou":
#       contador += 1
#
# Bonus: converta pra minusculas com palavra.lower() pra contar maiusculas
# tambem.
#
# VALIDACAO
# ---------
# "cabana" -> 3. "aeiou" -> 5. "xyz" -> 0. "CABANA" -> 3 (com lower()).
# =============================================================================


# >>> SEU CODIGO AQUI <<<
