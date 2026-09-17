# =============================================================================
# 073 - Modo append
# Nivel: 3 estrelas
# Conceitos: modo 'a'
# =============================================================================
#
# HISTORIA
# --------
# O diario da CabanaTerminal cresce todo dia. Se a gente abrir com "w", apaga
# tudo. O modo "a" (append) adiciona no fim sem destruir o que ja existe.
#
# TAREFA
# ------
# 1. Abra "diario.txt" em modo append ("a")
# 2. Peca uma anotacao ao usuario e grave com quebra de linha
# 3. Repita algumas vezes (rode o programa mais de uma vez)
# 4. No final, leia o arquivo e mostre que as anotacoes se acumularam
#
# Exemplo de execucao:
#
#   $ python3 073_modo_append.py
#   Anotacao: aprendi loops
#   Anotacao: aprendi strings
#   --- diario ---
#   aprendi loops
#   aprendi strings
#
# REQUISITOS
# ----------
# [ ] Usa open() com modo "a"
# [ ] Adiciona sem apagar o conteudo anterior
# [ ] Le e mostra o acumulado
#
# DICA
# ----
# No modo "w" o arquivo e zerado a cada abertura. No "a", o ponteiro vai pro
# fim. Nao esqueca o "\n" pra cada anotacao ficar numa linha.
#
# VALIDACAO
# ---------
# Rodar duas vezes mantem as anotacoes anteriores e adiciona a nova.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
