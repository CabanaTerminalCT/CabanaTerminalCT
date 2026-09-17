# =============================================================================
# 028 - Formata com estilo
# Nivel: 3 estrelas
# Conceitos: f-string avancada
# =============================================================================
#
# HISTORIA
# --------
# O painel da CabanaTerminal mostra dados alinhados: nome, pontos, media. Pra
# ficar bonito no terminal, a gente usa f-string com formatacao de largura,
# casas decimais e alinhamento.
#
# TAREFA
# ------
# 1. Peca o nome de um membro, os pontos e a media
# 2. Imprima uma linha formatada assim:
#
#   Nome:   eduardo
#   Pontos: 1234
#   Media:  8.50
#
# 3. Use a mesma f-string pra alinhar o nome em 10 colunas
#
# Exemplo de execucao:
#
#   $ python3 028_formata_com_estilo.py
#   Nome: eduardo
#   Pontos: 1234
#   Media: 8.50
#   |eduardo   |
#
# REQUISITOS
# ----------
# [ ] Usa f-string
# [ ] Formata a media com 2 casas: {media:.2f}
# [ ] Alinha o nome com largura: {nome:<10}
#
# DICA
# ----
# Dentro das chaves da f-string:
#   {valor:.2f}  -> 2 casas decimais
#   {texto:<10}  -> alinha a esquerda em 10 colunas
#   {texto:>10}  -> alinha a direita
#
# VALIDACAO
# ---------
# Media 8.5 -> "8.50". Nome "eduardo" -> "eduardo   " (3 espacos).
# =============================================================================


# >>> SEU CODIGO AQUI <<<
