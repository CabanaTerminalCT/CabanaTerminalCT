# =============================================================================
# 104 - Fluxo do menu
# Nivel: 4 estrelas
# Conceitos: UX basica, while, if/elif
# =============================================================================
#
# HISTORIA
# --------
# O usuario da CabanaTerminal nao le manual. O menu precisa ser obvio: opcoes
# numeradas, opcao de sair, resposta clara a cada acao. UX e parte do projeto.
#
# TAREFA
# ------
# 1. Desenhe o menu principal com as opcoes do seu projeto
# 2. Implemente o loop do menu com while
# 3. Cada opcao chama uma funcao (mesmo que ainda seja um stub)
# 4. Opcao invalida mostra aviso e volta ao menu
# 5. "sair" encerra com mensagem amigavel
#
# Exemplo de execucao:
#
#   $ python3 104_fluxo_do_menu.py
#   === PLACAR CTF CABANA ===
#   [1] adicionar [2] listar [3] buscar [0] sair
#   Opcao: 2
#   (nenhum registro)
#   Opcao: 9
#   Opcao invalida.
#   Opcao: 0
#   Ate a proxima!
#
# REQUISITOS
# ----------
# [ ] Menu com while
# [ ] if/elif pra cada opcao
# [ ] Opcao invalida tratada
# [ ] Saida limpa
#
# DICA
# ----
# Mostre o menu no topo de cada volta pra o usuario nunca se perder. Aceite
# "0" ou "sair" pra encerrar - de as duas formas.
#
# VALIDACAO
# ---------
# Navegar por todas as opcoes funciona; opcao invalida nao quebra; sair encerra.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
