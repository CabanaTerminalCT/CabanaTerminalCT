# =============================================================================
# 090 - Mini-projeto: sorteio de times
# Nivel: 4 estrelas
# Conceitos: random, listas, funcoes
# =============================================================================
#
# HISTORIA
# --------
# Todo mutirao da CabanaTerminal comeca com sorteio de times. Pra nao ter
# panelinha, o computador embaralha os membros e divide em equipes do mesmo
# tamanho. Este mini-projeto fecha o capitulo de modulos.
#
# TAREFA
# ------
# 1. Peca os nomes dos membros (ou use uma lista fixa) ate digitar "fim"
# 2. Peca em quantos times dividir
# 3. Embaralhe a lista com random.shuffle()
# 4. Divida em times equilibrados
# 5. Mostre cada time com seus membros
#
# Exemplo de execucao:
#
#   $ python3 090_sorteio_de_times.py
#   Nome (ou 'fim'): ana
#   Nome (ou 'fim'): bruno
#   Nome (ou 'fim'): carla
#   Nome (ou 'fim'): duda
#   Nome (ou 'fim'): fim
#   Quantos times? 2
#
#   === TIME 1 ===
#   bruno
#   ana
#   === TIME 2 ===
#   duda
#   carla
#
# REQUISITOS
# ----------
# [ ] Le membros num loop ate "fim"
# [ ] Usa random.shuffle()
# [ ] Divide em N times equilibrados
# [ ] Trata numero de times maior que o de membros
#
# DICAS
# -----
# - Um jeito simples de distribuir: percorra a lista embaralhada e jogue cada
#   membro no time i % n_times.
# - Se n_times > membros, avise que nao da pra formar tantos times.
#
# VALIDACAO
# ---------
# 4 membros em 2 times -> 2 e 2. 5 membros em 2 times -> um time com 3 e outro
# com 2. A ordem muda a cada execucao.
#
# Terminou? Voce fechou o Capitulo 9. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
