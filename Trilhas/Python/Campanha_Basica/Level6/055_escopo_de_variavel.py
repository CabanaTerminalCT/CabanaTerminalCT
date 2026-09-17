# =============================================================================
# 055 - Escopo de variavel
# Nivel: 3 estrelas
# Conceitos: local vs global
# =============================================================================
#
# HISTORIA
# --------
# Cada funcao da CabanaTerminal tem seu proprio "quintal": variaveis criadas
# dentro dela morrem ali. Entender escopo evita aquele bug classico de "por
# que essa variavel nao mudou?".
#
# TAREFA
# ------
# 1. Crie uma variavel global pontos = 0
# 2. Defina uma funcao que tenta alterar pontos localmente (sem global)
#    e mostre que a global nao muda
# 3. Defina uma funcao que declara "global pontos" e altera de verdade
# 4. Mostre o valor da global antes e depois
#
# Exemplo de execucao:
#
#   $ python3 055_escopo_de_variavel.py
#   Global antes: 0
#   Dentro (local): 10
#   Global depois do local: 0
#   Dentro (global): 10
#   Global depois do global: 10
#
# REQUISITOS
# ----------
# [ ] Mostra que variavel local nao afeta a global
# [ ] Usa a palavra-chave global numa funcao
# [ ] Comenta no codigo por que os valores mudam
#
# DICA
# ----
# Atribuir a "pontos" dentro da funcao cria uma variavel LOCAL com o mesmo
# nome. Pra mexer na global de verdade, declare "global pontos".
#
# VALIDACAO
# ---------
# A global so muda na segunda funcao, que usa global.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
