# =============================================================================
# 105 - Persistencia em JSON
# Nivel: 4 estrelas
# Conceitos: dados, json
# =============================================================================
#
# HISTORIA
# --------
# Um placar da CabanaTerminal que zera ao fechar nao serve. O projeto final
# precisa lembrar: carregar no inicio, salvar a cada alteracao (ou ao sair).
#
# TAREFA
# ------
# 1. Crie funcoes carregar_dados() e salvar_dados(dados)
# 2. carregar_dados le "dados.json" e devolve a estrutura; se nao existir,
#    devolve uma estrutura vazia
# 3. salvar_dados grava com indent=2 e ensure_ascii=False
# 4. Integre ao menu: carrega ao iniciar, salva ao sair
#
# Exemplo de execucao:
#
#   $ python3 105_persistencia_em_json.py
#   Carregando dados...
#   (arquivo nao existe, comecando vazio)
#   ... adiciona registros ...
#   Salvando 3 registros...
#   Feito!
#
# REQUISITOS
# ----------
# [ ] Funcao de carregar com tratamento de arquivo inexistente
# [ ] Funcao de salvar com json.dump
# [ ] Integrado ao fluxo do menu
#
# DICA
# ----
# Envolva o carregamento num try/except FileNotFoundError. A cada operacao que
# muda os dados, chame salvar_dados() - assim nada se perde se o programa
# fechar.
#
# VALIDACAO
# ---------
# Rodar, adicionar dados, sair e rodar de novo: os dados continuam la.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
