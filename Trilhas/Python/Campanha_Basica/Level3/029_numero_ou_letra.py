# =============================================================================
# 029 - E numero ou letra?
# Nivel: 3 estrelas
# Conceitos: .isdigit(), .isalpha(), .isalnum()
# =============================================================================
#
# HISTORIA
# --------
# Antes de aceitar um nick ou um ID no cadastro da CabanaTerminal, a gente
# valida o que o usuario digitou. Os metodos .is* dizem que tipo de conteudo a
# string tem.
#
# TAREFA
# ------
# 1. Peca um texto ao usuario
# 2. Diga se e so digitos
# 3. Diga se e so letras
# 4. Diga se e letras e/ou numeros
#
# Exemplo de execucao:
#
#   $ python3 029_numero_ou_letra.py
#   Texto: cabana123
#   So digitos? False
#   So letras? False
#   Alfanumerico? True
#
# REQUISITOS
# ----------
# [ ] Usa .isdigit()
# [ ] Usa .isalpha()
# [ ] Usa .isalnum()
#
# DICA
# ----
# - .isdigit()  -> True so se todos forem numeros
# - .isalpha()  -> True so se todos forem letras
# - .isalnum()  -> True se todos forem letras OU numeros
#
# Espaco e simbolos fazem todos retornarem False. String vazia tambem da
# False.
#
# VALIDACAO
# ---------
# "123" -> True, False, True. "abc" -> False, True, True.
# "abc123" -> False, False, True. "a b" -> False, False, False.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
