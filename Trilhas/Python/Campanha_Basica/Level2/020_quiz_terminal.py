# =============================================================================
# 020 - Mini-projeto: quiz do terminal
# Nivel: 4 estrelas
# Conceitos: tudo junto (input, if, for, while, acumulador)
# =============================================================================
#
# HISTORIA
# --------
# Chegou a prova final do Nivel 2. A CabanaTerminal vai te testar com um quiz
# de 5 perguntas sobre o que voce aprendeu ate aqui. No fim, o terminal mostra
# sua pontuacao e te da um veredito. Junta input, condicao, loop e acumulador
# num programa so.
#
# TAREFA
# ------
# 1. Prepare uma lista com 5 perguntas e suas respostas corretas
# 2. Use um for pra percorrer as perguntas
# 3. Pra cada uma, mostre a pergunta, leia a resposta e compare
# 4. Some 1 ponto por acerto
# 5. No final, mostre a pontuacao e uma mensagem conforme o desempenho
#
# Exemplo de execucao:
#
#   $ python3 020_quiz_terminal.py
#   === QUIZ CABANATERMINAL ===
#
#   Pergunta 1: Quanto e 2 + 2?
#   Resposta: 4
#   Correto!
#
#   Pergunta 2: Qual funcao le dados do usuario?
#   Resposta: input
#   Correto!
#   ...
#
#   === FIM ===
#   Voce acertou 4 de 5.
#   Muito bem, quase perfeito!
#
# REQUISITOS
# ----------
# [ ] Pelo menos 5 perguntas
# [ ] Usa for pra percorrer as perguntas
# [ ] Compara a resposta (dica: .lower().strip() ajuda a evitar erro de
#     espaco/maiuscula)
# [ ] Usa um acumulador de pontos
# [ ] Mostra pontuacao final com mensagem por faixa (ex: 5 = mestre,
#     3-4 = bom, menos de 3 = treine mais)
#
# DICAS
# -----
# - Guardar perguntas e respostas em duas listas alinhadas simplifica o loop:
#
#     perguntas = ["Quanto e 2 + 2?", "..."]
#     respostas = ["4", "..."]
#
#   E depois: "for i in range(len(perguntas)):"
#
# - Normalizar a resposta do usuario evita frustracao:
#
#     if resposta.strip().lower() == correta.lower():
#
# - Mostre a pergunta com o indice: f"Pergunta {i + 1}: ..."
#
# VALIDACAO
# ---------
# Acerte todas -> 5/5 e "mestre". Erre de proposito algumas e confira se a
# pontuacao e a mensagem mudam de acordo.
#
# Terminou? Voce fechou o Nivel 2. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
