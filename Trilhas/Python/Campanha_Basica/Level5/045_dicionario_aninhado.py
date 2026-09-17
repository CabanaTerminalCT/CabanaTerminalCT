# =============================================================================
# 045 - Dicionario aninhado
# Nivel: 4 estrelas
# Conceitos: dict dentro de dict
# =============================================================================
#
# HISTORIA
# --------
# O servidor da CabanaTerminal guarda varios membros, cada um com sua ficha
# completa. Isso e um dicionario de dicionarios - a estrutura que vira JSON na
# vida real.
#
# TAREFA
# ------
# 1. Crie um dict onde cada chave e um nick e o valor e outro dict (idade,
#    pontos)
# 2. Acesse os pontos de um membro especifico
# 3. Percorra todos os membros imprimindo nick, idade e pontos
# 4. Adicione um novo membro com sua propria ficha
#
# Exemplo de execucao:
#
#   $ python3 045_dicionario_aninhado.py
#   Pontos do dudu: 42
#   --- membros ---
#   dudu (20 anos): 42 pontos
#   ana (25 anos): 30 pontos
#   Novo membro adicionado.
#
# REQUISITOS
# ----------
# [ ] Cria dict de dicts
# [ ] Acessa valor aninhado (membros["dudu"]["pontos"])
# [ ] Percorre com .items() e acessa o dict interno
#
# DICA
# ----
# Pra percorrer, o valor de cada item tambem e um dict:
#
#   for nick, ficha in membros.items():
#       print(f"{nick}: {ficha['pontos']} pontos")
#
# VALIDACAO
# ---------
# Os pontos do membro certo aparecem e o novo membro entra na listagem.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
