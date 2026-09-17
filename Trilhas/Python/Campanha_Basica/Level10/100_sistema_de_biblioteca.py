# =============================================================================
# 100 - Mini-projeto: sistema de biblioteca
# Nivel: 4 estrelas
# Conceitos: classes, objetos, metodos, listas, JSON
# =============================================================================
#
# HISTORIA
# --------
# A CabanaTerminal montou uma biblioteca comunitaria: livros emprestados,
# devolvidos, disponiveis. Este mini-projeto fecha o capitulo de POO juntando
# classes, listas e persistencia num sistema de verdade.
#
# TAREFA
# ------
# 1. Crie a classe Livro(titulo, autor, disponivel=True)
# 2. Crie a classe Biblioteca com uma lista de livros
# 3. Metodos da Biblioteca:
#      - adicionar(livro)
#      - listar() -> mostra todos com status
#      - emprestar(titulo) -> marca indisponivel se estiver livre
#      - devolver(titulo) -> marca disponivel de novo
# 4. Menu em loop pra usar tudo
# 5. (Bonus) salvar e carregar a biblioteca de um JSON
#
# Exemplo de execucao:
#
#   $ python3 100_sistema_de_biblioteca.py
#   [1] listar [2] emprestar [3] devolver [4] adicionar [sair]
#   Opcao: 2
#   Titulo: Python Fluente
#   Emprestado! Bons estudos.
#   ...
#   Opcao: 1
#   [ ] Python Fluente - Luciano Ramalho (indisponivel)
#   [x] Estruturas de Dados - autor X (disponivel)
#
# REQUISITOS
# ----------
# [ ] Pelo menos duas classes
# [ ] Metodos que alteram o estado dos objetos
# [ ] Menu funcional com while
# [ ] Emprestar so se estiver disponivel; devolver so se estiver emprestado
# [ ] (Bonus) persistencia em JSON
#
# DICAS
# -----
# - Biblioteca pode guardar uma lista de objetos Livro.
# - Ache o livro com um for comparando titulo.
# - Use __str__ no Livro pra formatar a linha da listagem.
#
# VALIDACAO
# ---------
# Emprestar muda o status; tentar emprestar de novo avisa que ja esta fora;
# devolver libera de novo. Com JSON, o estado sobrevive ao fechar.
#
# Terminou? Voce fechou o Capitulo 10. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
