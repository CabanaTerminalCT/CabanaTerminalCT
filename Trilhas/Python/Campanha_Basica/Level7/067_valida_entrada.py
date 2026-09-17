# =============================================================================
# 067 - Valida entrada
# Nivel: 4 estrelas
# Conceitos: try + input em loop
# =============================================================================
#
# HISTORIA
# --------
# No cadastro da CabanaTerminal o usuario digita o que quer. Um bom programa
# insiste ate receber um dado valido, em vez de quebrar ou aceitar lixo. Aqui
# a gente junta try/except com while.
#
# TAREFA
# ------
# 1. Peca a idade em um loop
# 2. Se a entrada nao for numero, avise e peca de novo
# 3. Se for numero negativo, avise e peca de novo
# 4. So saia do loop quando a idade for valida e mostre a idade final
#
# Exemplo de execucao:
#
#   $ python3 067_valida_entrada.py
#   Idade: abc
#   Digite um numero valido.
#   Idade: -3
#   A idade nao pode ser negativa.
#   Idade: 20
#   Idade registrada: 20
#
# REQUISITOS
# ----------
# [ ] Usa while True com break
# [ ] Usa try/except pro int()
# [ ] Rejeita idade negativa
#
# DICA
# ----
# Só saia do loop com break quando passar nas duas checagens. O except cuida
# do texto invalido; o if cuida do numero fora do intervalo.
#
# VALIDACAO
# ---------
# "abc" e "-3" sao rejeitados; "20" encerra o loop e e registrado.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
