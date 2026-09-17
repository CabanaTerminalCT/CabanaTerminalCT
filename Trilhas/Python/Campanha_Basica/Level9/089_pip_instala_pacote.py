# =============================================================================
# 089 - PIP: instala pacote
# Nivel: 3 estrelas
# Conceitos: pip install
# =============================================================================
#
# HISTORIA
# --------
# A biblioteca padrao da CabanaTerminal e grande, mas nao tem tudo. Quando
# falta, a comunidade instala pacotes com o pip - o gerenciador de pacotes do
# Python. Este desafio e mais de terminal do que de codigo.
#
# TAREFA
# ------
# 1. No terminal, descubra a versao do pip: "pip --version"
# 2. Liste os pacotes instalados: "pip list"
# 3. Instale um pacote pequeno, ex: "pip install requests"
# 4. Confirme que ele aparece no pip list
# 5. Importe requests no Python e imprima a versao (requests.__version__)
#
# Exemplo de execucao:
#
#   $ pip install requests
#   Successfully installed requests-...
#   $ python3 089_pip_instala_pacote.py
#   requests versao: 2.31.0
#
# REQUISITOS
# ----------
# [ ] Rodou pip --version e pip list
# [ ] Instalou um pacote
# [ ] Importou o pacote no Python e mostrou a versao
#
# DICA
# ----
# Se "pip" nao funcionar, tente "pip3" ou "python3 -m pip". Em ambientes
# isolados, o ideal e usar venv antes de instalar:
#   python3 -m venv .venv && source .venv/bin/activate
#
# VALIDACAO
# ---------
# O pacote aparece no pip list e o import funciona sem erro.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
