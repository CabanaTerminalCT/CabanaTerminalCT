# =============================================================================
# 094 - Classe vs instancia
# Nivel: 4 estrelas
# Conceitos: atributo de classe vs de instancia
# =============================================================================
#
# HISTORIA
# --------
# Todos os membros da CabanaTerminal compartilham algumas coisas (o nome da
# comunidade) e tem outras proprias (o nick). Saber a diferenca entre atributo
# de classe e de instancia evita bug estranho.
#
# TAREFA
# ------
# 1. Crie a classe Membro com um atributo de CLASSE "comunidade =
#    'CabanaTerminal'"
# 2. No __init__, crie atributos de INSTANCIA (nome e pontos)
# 3. Crie dois membros
# 4. Mostre que comunidade e igual pra todos, mas nome/pontos sao proprios
# 5. Altere um atributo de classe e mostre o efeito em todos
#
# Exemplo de execucao:
#
#   $ python3 094_classe_vs_instancia.py
#   ana / bruno
#   Comunidade: CabanaTerminal
#   Mudei a comunidade...
#   Agora: CabanaTerminal CT
#
# REQUISITOS
# ----------
# [ ] Define atributo de classe (fora do __init__)
# [ ] Define atributos de instancia (dentro do __init__)
# [ ] Mostra a diferenca de comportamento
#
# DICA
# ----
# Atributo de classe fica direto no corpo da classe e e compartilhado. De
# instancia fica em self.* e e unico por objeto. Alterar a classe afeta todos
# que nao sobrescreveram.
#
# VALIDACAO
# ---------
# O valor da comunidade muda pra todos os objetos ao mesmo tempo.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
