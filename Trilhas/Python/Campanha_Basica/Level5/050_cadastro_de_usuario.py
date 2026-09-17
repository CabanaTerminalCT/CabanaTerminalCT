# =============================================================================
# 050 - Mini-projeto: cadastro de usuario
# Nivel: 4 estrelas
# Conceitos: dict, set, loops, validacao
# =============================================================================
#
# HISTORIA
# --------
# O cadastro da CabanaTerminal esta uma bagunca: nicks repetidos, fichas
# incompletas. Voce vai construir um pequeno sistema que registra membros num
# dicionario, recusa nick duplicado e no fim mostra um relatorio. Junta dict,
# set e loops num programa so.
#
# TAREFA
# ------
# 1. Fique cadastrando membros ate o usuario digitar "sair"
# 2. Pra cada membro, peca nick e pontos
# 3. Recuse nick ja cadastrado (use um set pra controlar)
# 4. Guarde os dados num dict: nick -> pontos
# 5. No fim, mostre:
#      - total de membros
#      - a lista de nicks (ordenada)
#      - o membro com mais pontos
#      - a media de pontos
#
# Exemplo de execucao:
#
#   $ python3 050_cadastro_de_usuario.py
#   Nick (ou 'sair'): dudu
#   Pontos: 42
#   dudu cadastrado!
#   Nick (ou 'sair'): dudu
#   Nick ja existe!
#   Nick (ou 'sair'): ana
#   Pontos: 30
#   ana cadastrada!
#   Nick (ou 'sair'): sair
#
#   === RELATORIO ===
#   Total: 2
#   Nicks: ['ana', 'dudu']
#   Lider: dudu (42)
#   Media: 36.0
#
# REQUISITOS
# ----------
# [ ] Usa dict pros dados e set pros nicks
# [ ] Recusa nick repetido
# [ ] Usa max() com key ou percorre pra achar o lider
# [ ] Trata cadastro vazio sem quebrar
#
# DICAS
# -----
# - Pra achar o lider: max(cadastro, key=cadastro.get) devolve o nick com
#   maior valor.
# - A media e sum(cadastro.values()) / len(cadastro).
#
# VALIDACAO
# ---------
# Cadastrar dudu(42), tentar dudu de novo (recusado), ana(30) -> total 2,
# lider dudu, media 36.0.
#
# Terminou? Voce fechou o Capitulo 5. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
