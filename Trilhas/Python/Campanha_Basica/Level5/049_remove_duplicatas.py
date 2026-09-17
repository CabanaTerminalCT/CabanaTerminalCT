# =============================================================================
# 049 - Remove duplicatas
# Nivel: 3 estrelas
# Conceitos: set + list
# =============================================================================
#
# HISTORIA
# --------
# A planilha de emails da CabanaTerminal veio cheia de repetidos. Antes de
# mandar o aviso do mutirao, voce precisa de uma lista limpa, sem duplicatas e
# de preferencia ordenada.
#
# TAREFA
# ------
# 1. Crie uma lista com valores repetidos
# 2. Converta pra set pra remover as duplicatas
# 3. Converta de volta pra lista
# 4. Ordene a lista final
#
# Exemplo de execucao:
#
#   $ python3 049_remove_duplicatas.py
#   Original: [3, 1, 3, 2, 1, 2]
#   Sem duplicatas: [1, 2, 3]
#
# REQUISITOS
# ----------
# [ ] Converte lista -> set -> lista
# [ ] Ordena o resultado
# [ ] Mostra original e final
#
# DICA
# ----
# A conversao e direta: list(set(lista)). Como set nao tem ordem, use
# sorted(...) pra garantir uma saida previsivel.
#
# VALIDACAO
# ---------
# [3,1,3,2,1,2] -> [1,2,3].
# =============================================================================


# >>> SEU CODIGO AQUI <<<
