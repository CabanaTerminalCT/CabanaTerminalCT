# =============================================================================
# 078 - Le JSON
# Nivel: 4 estrelas
# Conceitos: json.load()
# =============================================================================
#
# HISTORIA
# --------
# A configuracao da CabanaTerminal fica num arquivo JSON. Ao iniciar, o
# programa le esse arquivo e carrega os dados. Se o arquivo nao existir, a
# gente usa um padrao - sem quebrar.
#
# TAREFA
# ------
# 1. Crie um arquivo "config.json" com tema, volume e membros
# 2. Leia com json.load() e acesse os valores
# 3. Trate FileNotFoundError caso o arquivo nao exista
# 4. Se nao existir, crie um config padrao e avise
#
# Exemplo de execucao:
#
#   $ python3 078_le_json.py
#   Tema: hard-rock
#   Volume: 11
#   Membros: 3
#
# REQUISITOS
# ----------
# [ ] Importa json
# [ ] Usa json.load()
# [ ] Trata FileNotFoundError
#
# DICA
# ----
# Envolva a leitura num try/except FileNotFoundError. Assim o programa lida
# tanto com o arquivo presente quanto ausente.
#
# VALIDACAO
# ---------
# Com o arquivo, mostra os valores; sem o arquivo, avisa e cria o padrao.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
