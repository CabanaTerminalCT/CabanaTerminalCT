# =============================================================================
# 026 - Separa e junta
# Nivel: 3 estrelas
# Conceitos: .split(), .join()
# =============================================================================
#
# HISTORIA
# --------
# O log da CabanaTerminal chega numa linha so, separado por virgulas. Pra
# processar, a gente separa em pedacos com .split() e depois junta de novo
# com .join(). E a base de quase todo parsing.
#
# TAREFA
# ------
# 1. Peca uma frase com palavras separadas por virgula (ex: "a,b,c")
# 2. Separe em uma lista com .split(",")
# 3. Mostre a lista
# 4. Junte de volta com .join() usando " | " como separador
#
# Exemplo de execucao:
#
#   $ python3 026_separa_e_junta.py
#   Lista: cabana,ctf,python
#   Separado: ['cabana', 'ctf', 'python']
#   Junto: cabana | ctf | python
#
# REQUISITOS
# ----------
# [ ] Usa .split(",")
# [ ] Mostra a lista resultante
# [ ] Usa " | ".join(...) pra juntar
#
# DICA
# ----
# .split() sem argumento separa por espacos. .join() e chamado NO separador:
# " | ".join(lista).
#
# VALIDACAO
# ---------
# "cabana,ctf,python" -> 3 itens na lista e "cabana | ctf | python".
# =============================================================================


# >>> SEU CODIGO AQUI <<<
