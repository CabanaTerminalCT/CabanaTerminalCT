# =============================================================================
# 013 - Menu do terminal
# Nivel: 2 estrelas
# Conceitos: while + input
# =============================================================================
#
# HISTORIA
# --------
# O painel da CabanaTerminal precisa de um menu que fica rodando ate o
# operador mandar sair. Enquanto ninguem digita "sair", o programa continua
# mostrando as opcoes. Simples, mas e assim que metade dos CLIs do mundo
# funciona.
#
# TAREFA
# ------
# 1. Mostre um menu com 3 opcoes + "sair"
# 2. Peca uma opcao ao usuario
# 3. Repita ate ele digitar "sair"
# 4. Ao sair, imprima uma despedida
#
# Exemplo de execucao:
#
#   $ python3 013_menu_terminal.py
#   [1] Estudar trilha
#   [2] Resolver CTF
#   [3] Tomar cafe
#   [sair] Encerrar
#   Opcao: 1
#   -> Bora estudar!
#   ...
#   Opcao: sair
#   Encerrando o terminal da Cabana. Ate a proxima.
#
# REQUISITOS
# ----------
# [ ] O menu reaparece enquanto a opcao for diferente de "sair"
# [ ] Usa while com a condicao baseada no input
# [ ] Trata as opcoes 1, 2 e 3 com mensagens diferentes
# [ ] Opcao invalida tambem tem mensagem
#
# DICA
# ----
# Leia a opcao antes do loop e de novo no fim de cada volta:
#
#   opcao = ""
#   while opcao != "sair":
#       print("menu...")
#       opcao = input("Opcao: ")
#
# VALIDACAO
# ---------
# Digite 1, 2, 3, algo invalido e por fim "sair". O loop so termina no sair.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
