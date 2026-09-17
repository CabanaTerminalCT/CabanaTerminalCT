# =============================================================================
# 009 - Senao, aquilo outro
# Nivel: 2 estrelas
# Conceitos: if / else
# =============================================================================
#
# HISTORIA
# --------
# No desafio anterior, quem errava a senha nao recebia resposta. Isso e ruim
# de UX e pessimo pra seguranca. Agora a CabanaTerminal sempre responde:
# acesso liberado ou acesso negado.
#
# TAREFA
# ------
# 1. Peca a senha ao usuario
# 2. Se for "cabana", imprime: [ OK ] Acesso liberado.
# 3. Senao, imprime: [ ERRO ] Senha incorreta. Tente de novo.
#
# Exemplo de execucao:
#
#   $ python3 009_else.py
#   Senha: cabana
#   [ OK ] Acesso liberado.
#
#   $ python3 009_else.py
#   Senha: 1234
#   [ ERRO ] Senha incorreta. Tente de novo.
#
# REQUISITOS
# ----------
# [ ] Usa if E else
# [ ] O else nao tem condicao (nao escreve "else senha == ...")
# [ ] Os dois caminhos imprimem algo
#
# DICA
# ----
# else e o "caso contrario" - pega tudo que nao entrou no if. Nao leva
# condicao e termina com dois-pontos.
#
# VALIDACAO
# ---------
# Teste com a senha certa e com uma errada. Os dois ramos tem que funcionar.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
