# =============================================================================
# 098 - Encapsulamento
# Nivel: 4 estrelas
# Conceitos: _atributo (protegido)
# =============================================================================
#
# HISTORIA
# --------
# Nem todo dado de um membro da CabanaTerminal deve ser mexido direto. A senha,
# por exemplo, nao pode ficar solta. Encapsulamento e o acordo de acessar
# certos atributos so por metodos controlados.
#
# TAREFA
# ------
# 1. Crie a classe Conta com __init__(titular, saldo=0)
# 2. Guarde o saldo num atributo "protegido": _saldo
# 3. Crie metodos depositar(valor) e sacar(valor) que alteram _saldo com
#    validacao
# 4. Crie um getter saldo() que devolve o _saldo
# 5. Tente acessar _saldo direto e comente por que nao se deve
#
# Exemplo de execucao:
#
#   $ python3 098_encapsulamento.py
#   Saldo: 100
#   Saque de 30 ok. Saldo: 70
#   Saque de 100 recusado (saldo insuficiente).
#
# REQUISITOS
# ----------
# [ ] Usa atributo com underline (_saldo)
# [ ] Altera o saldo so por metodos
# [ ] Valida saque maior que o saldo
#
# DICA
# ----
# O underline e uma convencao: "isso e interno, nao mexe direto". Python nao
# bloqueia, mas a comunidade respeita. Use metodos pra manter as regras.
#
# VALIDACAO
# ---------
# Deposito e saque valido alteram o saldo; saque acima do saldo e recusado.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
