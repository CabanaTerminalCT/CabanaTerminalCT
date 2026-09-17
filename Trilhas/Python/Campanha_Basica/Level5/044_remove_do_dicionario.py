# =============================================================================
# 044 - Remove do dicionario
# Nivel: 3 estrelas
# Conceitos: pop, del, clear
# =============================================================================
#
# HISTORIA
# --------
# Membro saiu da CabanaTerminal? Precisa remover a ficha. As vezes voce quer
# saber o valor removido (pop), as vezes so apagar (del), as vezes limpar tudo
# (clear).
#
# TAREFA
# ------
# 1. Crie um dict com 3 membros e pontos
# 2. Remova um membro com .pop() e mostre os pontos dele
# 3. Remova outro com del
# 4. Mostre o dict restante
# 5. Limpe tudo com .clear() e mostre vazio
#
# Exemplo de execucao:
#
#   $ python3 044_remove_do_dicionario.py
#   Removido bruno: 20
#   Depois do del: {'carla': 15}
#   Depois do clear: {}
#
# REQUISITOS
# ----------
# [ ] Usa .pop() e mostra o valor retornado
# [ ] Usa del
# [ ] Usa .clear()
#
# DICA
# ----
# - placar.pop("bruno")      -> remove e devolve 20
# - del placar["carla"]      -> remove sem devolver
# - placar.clear()           -> esvazia o dict
#
# .pop() com chave inexistente da KeyError; passe um padrao pro segundo
# argumento se quiser evitar.
#
# VALIDACAO
# ---------
# A saida mostra a remocao com valor, o dict reduzido e o dict vazio.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
