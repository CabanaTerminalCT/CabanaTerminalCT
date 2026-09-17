# =============================================================================
# 046 - Contador de palavras
# Nivel: 4 estrelas
# Conceitos: dict como acumulador
# =============================================================================
#
# HISTORIA
# --------
# O log da CabanaTerminal tem milhares de palavras e alguem quer saber quais
# aparecem mais. Contar ocorrencias com dicionario e um dos usos mais classicos
# e poderosos de dict.
#
# TAREFA
# ------
# 1. Peca uma frase ao usuario
# 2. Separe em palavras com .split()
# 3. Conte quantas vezes cada palavra aparece usando um dict
# 4. Imprima o resultado no formato "palavra: quantidade"
#
# Exemplo de execucao:
#
#   $ python3 046_contador_de_palavras.py
#   Frase: cabana cabana ctf
#   cabana: 2
#   ctf: 1
#
# REQUISITOS
# ----------
# [ ] Usa .split() pra separar
# [ ] Usa dict pra acumular contagens
# [ ] Percorre o dict no final
#
# DICA
# ----
# A chave e a palavra; o valor e a contagem. Se ja existe, soma 1; se nao,
# comeca em 1:
#
#   contagem[palavra] = contagem.get(palavra, 0) + 1
#
# Bonus: converta pra minusculas antes, pra "Cabana" e "cabana" contarem
# juntas.
#
# VALIDACAO
# ---------
# "cabana cabana ctf" -> cabana: 2, ctf: 1.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
