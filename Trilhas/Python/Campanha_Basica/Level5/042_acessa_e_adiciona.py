# =============================================================================
# 042 - Acessa e adiciona
# Nivel: 3 estrelas
# Conceitos: .get(), .setdefault()
# =============================================================================
#
# HISTORIA
# --------
# Nem toda ficha da CabanaTerminal tem todos os campos. Se voce acessar uma
# chave que nao existe direto, o programa quebra com KeyError. A solucao e
# acessar com seguranca usando .get().
#
# TAREFA
# ------
# 1. Crie um dict com nome e pontos
# 2. Tente acessar "email" com .get() - deve devolver None (ou um padrao)
# 3. Use .get("email", "sem email") pra dar valor padrao
# 4. Adicione a chave "email" com .setdefault()
# 5. Mostre o dict final
#
# Exemplo de execucao:
#
#   $ python3 042_acessa_e_adiciona.py
#   Email (get): None
#   Email (padrao): sem email
#   Final: {'nome': 'ana', 'pontos': 10, 'email': 'nao informado'}
#
# REQUISITOS
# ----------
# [ ] Usa .get() sem padrao
# [ ] Usa .get() com valor padrao
# [ ] Usa .setdefault()
#
# DICA
# ----
# - ficha.get("email")           -> None se nao existir
# - ficha.get("email", "nada")   -> "nada" se nao existir
# - ficha.setdefault("email", x) -> cria a chave so se ela nao existir
#
# VALIDACAO
# ---------
# Acessos a chave inexistente nao quebram; o dict termina com "email".
# =============================================================================


# >>> SEU CODIGO AQUI <<<
