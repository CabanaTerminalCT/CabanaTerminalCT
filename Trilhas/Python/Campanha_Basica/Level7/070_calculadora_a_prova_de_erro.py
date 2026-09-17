# =============================================================================
# 070 - Mini-projeto: calculadora a prova de erro
# Nivel: 4 estrelas
# Conceitos: try/except/else/finally, funcoes, loop
# =============================================================================
#
# HISTORIA
# --------
# A calculadora do capitulo anterior quebrava com entrada ruim. Agora a
# CabanaTerminal quer uma versao profissional: nao morre nunca, avisa o
# usuario e continua rodando ate ele mandar sair. Este e o mini-projeto que
# fecha o capitulo de erros.
#
# TAREFA
# ------
# 1. Reaproveite as funcoes somar, subtrair, multiplicar e dividir
# 2. Menu em loop ate "sair"
# 3. Trate ValueError (entrada nao numerica) e ZeroDivisionError
# 4. Use else pra mostrar o resultado so quando deu certo
# 5. Use finally pra imprimir um separador a cada operacao
#
# Exemplo de execucao:
#
#   $ python3 070_calculadora_a_prova_de_erro.py
#   [1] somar  [2] subtrair  [3] multiplicar  [4] dividir  [sair]
#   Operacao: 4
#   Numero 1: 10
#   Numero 2: 0
#   Nao da pra dividir por zero.
#   ----------
#   Operacao: 1
#   Numero 1: abc
#   Entrada invalida, digite numeros.
#   ----------
#   Operacao: sair
#   Ate a proxima!
#
# REQUISITOS
# ----------
# [ ] Funcoes separadas por operacao
# [ ] try/except/else/finally no fluxo
# [ ] Nenhuma entrada derruba o programa
# [ ] Opcao invalida do menu tambem tratada
#
# DICAS
# -----
# - Converta as entradas dentro do try.
# - Coloque a chamada da operacao no else, pra nao rodar se a conversao
#   falhou.
# - finally pode imprimir "----------" separando cada rodada.
#
# VALIDACAO
# ---------
# Dividir por zero -> aviso; digitar "abc" -> aviso; o menu continua ate
# "sair".
#
# Terminou? Voce fechou o Capitulo 7. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
