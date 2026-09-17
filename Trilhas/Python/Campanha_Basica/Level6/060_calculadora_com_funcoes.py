# =============================================================================
# 060 - Mini-projeto: calculadora com funcoes
# Nivel: 4 estrelas
# Conceitos: funcoes, menu, loops
# =============================================================================
#
# HISTORIA
# --------
# A CabanaTerminal precisa de uma calculadora de linha de comando. Cada
# operacao vira uma funcao propria e um menu chama a funcao certa. Este
# mini-projeto junta tudo do capitulo de funcoes.
#
# TAREFA
# ------
# 1. Crie uma funcao pra cada operacao: somar, subtrair, multiplicar, dividir
# 2. Mostre um menu que repete ate o usuario digitar "sair"
# 3. Leia dois numeros e a operacao
# 4. Chame a funcao certa e mostre o resultado
# 5. Trate divisao por zero com uma mensagem amigavel
#
# Exemplo de execucao:
#
#   $ python3 060_calculadora_com_funcoes.py
#   [1] somar  [2] subtrair  [3] multiplicar  [4] dividir  [sair]
#   Operacao: 1
#   Numero 1: 7
#   Numero 2: 5
#   Resultado: 12
#   ...
#   Operacao: sair
#   Ate a proxima!
#
# REQUISITOS
# ----------
# [ ] Uma funcao por operacao
# [ ] Menu com while
# [ ] Cada funcao recebe dois numeros e retorna o resultado
# [ ] Divisao por zero tratada
#
# DICAS
# -----
# - Converta os numeros com float() pra aceitar decimais.
# - Deixe o menu num loop e use if/elif pra escolher a funcao.
# - Se divisor == 0, imprima um aviso em vez de deixar quebrar.
#
# VALIDACAO
# ---------
# 7 + 5 -> 12; 7 / 0 -> mensagem de erro; "sair" encerra o programa.
#
# Terminou? Voce fechou o Capitulo 6. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
