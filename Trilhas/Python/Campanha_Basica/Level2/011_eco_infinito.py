# =============================================================================
# 011 - Eco infinito
# Nivel: 2 estrelas
# Conceitos: while
# =============================================================================
#
# HISTORIA
# --------
# A CabanaTerminal tem um servidor de IRC meio zoado que fica repetindo
# mensagens. Voce foi escalado pra escrever o "eco": repete a mesma frase
# varias vezes, controlado por um contador. Loop e a alma do terminal.
#
# TAREFA
# ------
# 1. Peca uma mensagem ao usuario
# 2. Peca quantas vezes repetir (numero inteiro)
# 3. Use um while pra imprimir a mensagem exatamente esse numero de vezes
#
# Exemplo de execucao:
#
#   $ python3 011_eco_infinito.py
#   Mensagem: Cabana
#   Quantas vezes? 3
#   Cabana
#   Cabana
#   Cabana
#
# REQUISITOS
# ----------
# [ ] Usa while (nao vale for neste desafio)
# [ ] Imprime exatamente N vezes, nem uma a mais
# [ ] O contador e incrementado dentro do loop
#
# DICA
# ----
# Precisamos de uma variavel de controle que cresce a cada volta:
#
#   i = 0
#   while i < vezes:
#       print(mensagem)
#       i += 1
#
# Se esquecer o "i += 1", o loop nunca termina. Ctrl+C e seu amigo.
#
# VALIDACAO
# ---------
# Com 3, imprime 3 linhas. Com 0, nao imprime nada. Com 1, imprime 1.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
