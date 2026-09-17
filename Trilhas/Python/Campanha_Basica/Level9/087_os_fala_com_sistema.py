# =============================================================================
# 087 - OS: fala com sistema
# Nivel: 4 estrelas
# Conceitos: os
# =============================================================================
#
# HISTORIA
# --------
# Scripts da CabanaTerminal precisam saber onde estao, listar arquivos e ler
# variaveis de ambiente. O modulo os e a ponte entre o Python e o sistema
# operacional.
#
# TAREFA
# ------
# 1. Mostre o diretorio atual com os.getcwd()
# 2. Liste os arquivos da pasta com os.listdir()
# 3. Leia uma variavel de ambiente (ex: HOME) com os.environ.get()
# 4. Monte um caminho com os.path.join() e verifique se existe
#
# Exemplo de execucao:
#
#   $ python3 087_os_fala_com_sistema.py
#   Diretorio atual: /home/eduardo
#   Arquivos: ['Documentos', 'Downloads', ...]
#   HOME: /home/eduardo
#   Caminho existe? True
#
# REQUISITOS
# ----------
# [ ] Importa os
# [ ] Usa os.getcwd() e os.listdir()
# [ ] Usa os.environ.get()
# [ ] Usa os.path.join()
#
# DICA
# ----
# os.environ.get("HOME") devolve None se a variavel nao existir - bem mais
# seguro que os.environ["HOME"], que daria KeyError.
#
# VALIDACAO
# ---------
# O diretorio, a listagem e a variavel de ambiente aparecem corretos.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
