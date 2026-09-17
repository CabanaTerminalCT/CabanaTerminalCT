# =============================================================================
# 095 - Heranca
# Nivel: 4 estrelas
# Conceitos: classe filha
# =============================================================================
#
# HISTORIA
# --------
# Na CabanaTerminal todo membro tem nome e pontos. Mas mentor tambem tem
# especialidade e novato tem trilha atual. Heranca deixa a classe Mentor
# reaproveitar tudo de Membro e so acrescentar o que e novo.
#
# TAREFA
# ------
# 1. Crie a classe Membro com __init__(nome, pontos) e metodo apresentar()
# 2. Crie a classe Mentor(Membro) que adiciona especialidade
# 3. No __init__ do Mentor, chame super().__init__(...) e guarde a
#    especialidade
# 4. Crie um Mentor e mostre que ele tem os atributos e metodos herdados
#
# Exemplo de execucao:
#
#   $ python3 095_heranca.py
#   Sou ana, 30 pontos.
#   Especialidade: seguranca
#
# REQUISITOS
# ----------
# [ ] Classe filha herda da mae: class Mentor(Membro)
# [ ] Usa super() no __init__
# [ ] Mentor usa metodo herdado de Membro
#
# DICA
# ----
# super().__init__(nome, pontos) roda o construtor da classe mae, entao voce
# so cuida do que e especifico da filha.
#
# VALIDACAO
# ---------
# O Mentor tem nome, pontos (herdados) e especialidade (proprio), e apresentar()
# funciona.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
