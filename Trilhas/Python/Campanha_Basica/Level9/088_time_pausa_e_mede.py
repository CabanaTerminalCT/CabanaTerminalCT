# =============================================================================
# 088 - Time: pausa e mede
# Nivel: 3 estrelas
# Conceitos: time
# =============================================================================
#
# HISTORIA
# --------
# Aquela tela de "carregando..." da CabanaTerminal existe por causa de pausas.
# E quando a gente quer saber quanto tempo um codigo demora, o modulo time
# cronometra.
#
# TAREFA
# ------
# 1. Importe time
# 2. Imprima uma contagem de 3 a 1 com pausa de 1 segundo (time.sleep)
# 3. Depois de "vai!", meça o tempo de um loop pesado com time.time()
# 4. Mostre quanto tempo o loop levou
#
# Exemplo de execucao:
#
#   $ python3 088_time_pausa_e_mede.py
#   3...
#   2...
#   1...
#   Vai!
#   Loop levou 0.0123 segundos
#
# REQUISITOS
# ----------
# [ ] Usa time.sleep()
# [ ] Usa time.time() antes e depois
# [ ] Calcula e mostra a diferenca
#
# DICA
# ----
# Guarde inicio = time.time(), rode o codigo e calcule time.time() - inicio.
# O resultado vem em segundos, com casas decimais.
#
# VALIDACAO
# ---------
# A contagem tem pausa real de ~1s entre os numeros e o tempo do loop aparece.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
