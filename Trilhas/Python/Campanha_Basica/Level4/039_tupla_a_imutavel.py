# =============================================================================
# 039 - Tupla: a imutavel
# Nivel: 4 estrelas
# Conceitos: tuple, empacotamento/desempacotamento
# =============================================================================
#
# HISTORIA
# --------
# Nem tudo na CabanaTerminal deve mudar. As coordenadas de um desafio de CTF
# sao fixas - se alguem alterar, quebra tudo. Pra isso existe a tupla: uma
# sequencia que nao pode ser modificada depois de criada.
#
# TAREFA
# ------
# 1. Crie uma tupla com coordenadas (latitude, longitude)
# 2. Mostre a tupla e acesse cada valor por indice
# 3. Desempacote a tupla em duas variaveis e imprima
# 4. Tente alterar um valor e observe o erro (TypeError)
#
# Exemplo de execucao:
#
#   $ python3 039_tupla_a_imutavel.py
#   Coordenadas: (-23.55, -46.63)
#   Latitude: -23.55
#   Longitude: -46.63
#   TypeError: 'tuple' object does not support item assignment
#
# REQUISITOS
# ----------
# [ ] Cria uma tupla com parenteses
# [ ] Desempacota em variaveis
# [ ] Comenta o motivo do erro ao tentar alterar
#
# DICA
# ----
# Desempacotar: "lat, lon = coordenadas". Alterar "coordenadas[0] = 0" levanta
# TypeError porque tuplas sao imutaveis. Se precisar mudar, use lista.
#
# VALIDACAO
# ---------
# A saida mostra os valores, o desempacotamento e o erro esperado.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
