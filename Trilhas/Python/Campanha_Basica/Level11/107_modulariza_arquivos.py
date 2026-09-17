# =============================================================================
# 107 - Modulariza arquivos
# Nivel: 4 estrelas
# Conceitos: arquitetura, modulos
# =============================================================================
#
# HISTORIA
# --------
# Um arquivo de 500 linhas e dificil de manter. A CabanaTerminal separa o
# projeto em modulos: um pro menu, um pros dados, um pra logica. Assim cada
# parte vive no seu canto.
#
# TAREFA
# ------
# 1. Separe seu projeto em pelo menos 2 arquivos:
#      - dados.py  -> carregar, salvar, CRUD
#      - main.py   -> menu e fluxo (importa de dados)
# 2. Mantenha cada modulo com uma responsabilidade clara
# 3. No main.py, importe as funcoes de dados.py
# 4. Comente o desenho da arquitetura no topo
#
# Exemplo de execucao:
#
#   $ python3 107_modulariza_arquivos.py
#   Arquitetura:
#     dados.py -> persistencia e CRUD
#     main.py  -> menu e fluxo
#   Rodando via main...
#
# REQUISITOS
# ----------
# [ ] Pelo menos 2 arquivos .py
# [ ] main.py importa de dados.py
# [ ] Responsabilidades separadas
#
# DICA
# ----
# Dica de ouro: se main.py ficar grande, crie mais modulos. Um bom sinal e
# conseguir testar dados.py sem abrir menu nenhum.
#
# VALIDACAO
# ---------
# O programa roda a partir do main.py usando as funcoes do outro modulo.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
