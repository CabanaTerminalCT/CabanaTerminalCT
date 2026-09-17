# =============================================================================
# 010 - Mini-projeto: classifica idade
# Nivel: 3 estrelas
# Conceitos: if / elif / else + input
# =============================================================================
#
# HISTORIA
# --------
# A CabanaTerminal e feita de gente de todo tipo: novatos, veteranos, quem ta
# comecando hoje e quem ja quebrou muita coisa no terminal. Pra organizar os
# mutiroes por faixa de experiencia, voce vai escrever um programa que
# classifica a pessoa pela idade e da um titulo dentro da comunidade.
#
# Este e o mini-projeto do Nivel 1: junta tudo o que voce aprendeu - input,
# conversao de tipo, comparacao e decisao encadeada.
#
# TAREFA
# ------
# 1. Peca o nome do usuario
# 2. Peca a idade (numero inteiro)
# 3. Classifique a pessoa conforme a tabela abaixo
# 4. Imprima uma mensagem personalizada com nome, idade e classificacao
#
# TABELA DE CLASSIFICACAO
# -----------------------
#   ate 12 anos        -> Curioso  - bem-vindo pra aprender brincando
#   13 a 17 anos       -> Aprendiz - ja pode encarar trilha e CTF facil
#   18 a 59 anos       -> Membro   - mao na massa, pode ate mentorar
#   60 anos ou mais    -> Veterano - respeito total, historia viva
#
# Exemplo de execucao:
#
#   $ python3 010_classifica_idade.py
#   Qual seu nome? Eduardo
#   Qual sua idade? 20
#   Salve, Eduardo! Com 20 anos voce e Membro na CabanaTerminal.
#
# REQUISITOS
# ----------
# [ ] Usa input() para nome e idade
# [ ] Converte a idade com int()
# [ ] Usa if / elif / else cobrindo as 4 faixas
# [ ] A mensagem final inclui nome, idade e classificacao (use f-string)
# [ ] Trata idade negativa ou impossivel com uma mensagem de erro (idade < 0)
#
# DICAS
# -----
# - Comece do menor pro maior (ou use "and" nas condicoes), pra nao sobrepor
#   faixas:
#
#     if idade <= 12:
#         classe = "Curioso"
#     elif idade <= 17:
#         classe = "Aprendiz"
#     elif idade <= 59:
#         classe = "Membro"
#     else:
#         classe = "Veterano"
#
# - Guardar a classificacao numa variavel e imprimir so no final deixa o
#   codigo mais limpo.
# - Lembre: int() quebra se o usuario digitar letras. Tratar isso e bonus.
#
# VALIDACAO
# ---------
#   Entrada 8  -> Curioso
#   Entrada 15 -> Aprendiz
#   Entrada 30 -> Membro
#   Entrada 70 -> Veterano
#   Entrada -3 -> mensagem de erro
#
# Depois de terminar, voce fechou o Nivel 1. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
