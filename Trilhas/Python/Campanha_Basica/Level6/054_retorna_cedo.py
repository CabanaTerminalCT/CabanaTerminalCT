# =============================================================================
# 054 - Retorna cedo
# Nivel: 3 estrelas
# Conceitos: return no meio da funcao
# =============================================================================
#
# HISTORIA
# --------
# Nem toda verificacao precisa ir ate o fim. Se o dado ja esta invalido, a
# funcao da CabanaTerminal pode devolver a resposta e sair na hora com return.
# Isso deixa o codigo mais limpo e rapido.
#
# TAREFA
# ------
# 1. Defina classificar(nota) que:
#      - retorna "invalida" se nota < 0 ou > 10
#      - retorna "reprovado" se nota < 6
#      - retorna "aprovado" caso contrario
# 2. Teste com -1, 5 e 8
#
# Exemplo de execucao:
#
#   $ python3 054_retorna_cedo.py
#   -1 -> invalida
#   5 -> reprovado
#   8 -> aprovado
#
# REQUISITOS
# ----------
# [ ] Usa return no meio da funcao pra sair cedo
# [ ] Cobre os tres casos
# [ ] Chama a funcao em varios testes
#
# DICA
# ----
# return encerra a funcao imediatamente - o que vier depois dele nao roda.
# Por isso a checagem de invalido vem primeiro.
#
# VALIDACAO
# ---------
# -1 -> invalida, 5 -> reprovado, 8 -> aprovado.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
