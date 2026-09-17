# =============================================================================
# 030 - Mini-projeto: validador de senha
# Nivel: 4 estrelas
# Conceitos: strings (len, is*, in, loops)
# =============================================================================
#
# HISTORIA
# --------
# O cadastro da CabanaTerminal precisa de senhas decentes. Nada de "1234".
# Voce vai escrever o validador que aprova ou reprova uma senha segundo
# regras de seguranca. Junta tudo do capitulo de strings num programa so.
#
# TAREFA
# ------
# Peca uma senha e verifique TODAS as regras:
#
#   1. Tem pelo menos 8 caracteres
#   2. Tem pelo menos uma letra maiuscula
#   3. Tem pelo menos uma letra minuscula
#   4. Tem pelo menos um numero
#   5. Tem pelo menos um caractere especial (!@#$% etc.)
#
# Mostre quais regras passaram e quais falharam e, no final, se a senha e
# valida ou nao.
#
# Exemplo de execucao:
#
#   $ python3 030_validador_de_senha.py
#   Senha: Cabana#2026
#   [ OK ] 8+ caracteres
#   [ OK ] tem maiuscula
#   [ OK ] tem minuscula
#   [ OK ] tem numero
#   [ OK ] tem especial
#   Senha valida!
#
# REQUISITOS
# ----------
# [ ] Verifica as 5 regras
# [ ] Mostra o status de cada regra
# [ ] No fim, aprova ou reprova
#
# DICAS
# -----
# - Percorra a senha com um for e use flags booleanas:
#
#     tem_maiuscula = False
#     for c in senha:
#         if c.isupper():
#             tem_maiuscula = True
#
# - Pra especial, cheque o contrario: se NAO for alfanumerico e NAO for
#   espaco, entao e especial.
# - len(senha) >= 8 resolve a primeira regra.
#
# VALIDACAO
# ---------
# "Cabana#2026" -> valida. "cabana" -> reprovada (curta, sem maiuscula, sem
# numero, sem especial).
#
# Terminou? Voce fechou o Capitulo 3. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
