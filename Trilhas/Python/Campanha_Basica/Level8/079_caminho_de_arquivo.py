# =============================================================================
# 079 - Caminho de arquivo
# Nivel: 4 estrelas
# Conceitos: pathlib
# =============================================================================
#
# HISTORIA
# --------
# Montar caminho com strings e coisa do passado - uma barra errada e quebra em
# outro sistema. pathlib trata caminhos como objetos e funciona em Linux,
# Mac e Windows.
#
# TAREFA
# ------
# 1. Importe Path de pathlib
# 2. Monte um caminho pra uma pasta "dados" dentro da pasta atual
# 3. Crie a pasta com .mkdir() (sem erro se ja existir)
# 4. Crie um arquivo dentro dela e verifique se existe com .exists()
# 5. Mostre o nome e a extensao do arquivo
#
# Exemplo de execucao:
#
#   $ python3 079_caminho_de_arquivo.py
#   Pasta: dados
#   Arquivo existe? True
#   Nome: notas.txt
#   Extensao: .txt
#
# REQUISITOS
# ----------
# [ ] Importa Path de pathlib
# [ ] Usa o operador / pra juntar caminhos
# [ ] Usa .mkdir(exist_ok=True) e .exists()
#
# DICA
# ----
# Path("dados") / "notas.txt" monta o caminho sem se preocupar com barras.
# .mkdir(exist_ok=True) evita erro se a pasta ja existir.
#
# VALIDACAO
# ---------
# A pasta dados e o arquivo notas.txt sao criados; o programa confirma a
# existencia e mostra nome/extensao.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
