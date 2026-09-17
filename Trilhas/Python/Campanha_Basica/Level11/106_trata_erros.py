# =============================================================================
# 106 - Trata erros
# Nivel: 4 estrelas
# Conceitos: robustez, try/except
# =============================================================================
#
# HISTORIA
# --------
# Projeto de verdade nao pode morrer porque o usuario digitou letra onde
# queria numero. A CabanaTerminal quer um programa que aguenta desaforo:
# entrada ruim, arquivo corrompido, campo vazio.
#
# TAREFA
# ------
# 1. Revise seu projeto e liste os pontos que podem falhar:
#      - conversao de numero
#      - arquivo JSON inexistente ou corrompido
#      - campos vazios
#      - indice/registro nao encontrado
# 2. Adicione try/except nesses pontos, com mensagens claras
# 3. Garanta que NENHUMA entrada derruba o programa
# 4. Comente cada tratamento explicando o que ele protege
#
# Exemplo de execucao:
#
#   $ python3 106_trata_erros.py
#   Opcao: abc
#   Digite um numero valido.
#   Opcao: 2
#   (lista vazia)
#   Arquivo corrompido? Recuperando com dados vazios...
#
# REQUISITOS
# ----------
# [ ] Trata conversao de entrada
# [ ] Trata JSON inexistente/corrompido
# [ ] Trata busca sem resultado
# [ ] Nenhum crash em uso normal
#
# DICA
# ----
# Trate o erro ESPECIFICO (ValueError, FileNotFoundError, json.JSONDecodeError),
# nao um except generico que esconde tudo.
#
# VALIDACAO
# ---------
# Tente quebrar de proposito: texto no lugar de numero, JSON invalido, buscar
# inexistente. O programa continua de pe.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
