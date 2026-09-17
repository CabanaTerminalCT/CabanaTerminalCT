# =============================================================================
# 056 - Funcao que chama funcao
# Nivel: 3 estrelas
# Conceitos: composicao
# =============================================================================
#
# HISTORIA
# --------
# Na CabanaTerminal a gente resolve problema grande quebrando em pedacos
# pequenos. Cada funcao faz uma coisa, e uma funcao chama as outras pra montar
# o resultado. Isso e composicao.
#
# TAREFA
# ------
# 1. Defina area_retangulo(base, altura) que retorna base * altura
# 2. Defina area_triangulo(base, altura) que usa area_retangulo e divide por 2
# 3. Defina resumo(base, altura) que imprime as duas areas usando as funcoes
# 4. Chame resumo(10, 4)
#
# Exemplo de execucao:
#
#   $ python3 056_funcao_que_chama_funcao.py
#   Retangulo: 40
#   Triangulo: 20
#
# REQUISITOS
# ----------
# [ ] Uma funcao chama outra
# [ ] Nenhuma logica duplicada (triangulo reusa retangulo)
# [ ] Pelo menos tres funcoes
#
# DICA
# ----
# area_triangulo nao precisa repetir a multiplicacao: ela chama
# area_retangulo(base, altura) / 2.
#
# VALIDACAO
# ---------
# resumo(10,4) -> retangulo 40, triangulo 20.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
