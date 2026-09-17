# =============================================================================
# 071 - Escreve no arquivo
# Nivel: 3 estrelas
# Conceitos: open(), write()
# =============================================================================
#
# HISTORIA
# --------
# Ate agora tudo que a CabanaTerminal fazia sumia quando o programa fechava.
# Arquivos mudam isso: a gente grava um texto e ele continua la amanha. O
# primeiro passo e escrever.
#
# TAREFA
# ------
# 1. Peca uma mensagem ao usuario
# 2. Abra (ou crie) o arquivo "cabana.txt" em modo escrita ("w")
# 3. Escreva a mensagem no arquivo
# 4. Feche o arquivo e confirme na tela
#
# Exemplo de execucao:
#
#   $ python3 071_escreve_no_arquivo.py
#   Mensagem: salve, cabana!
#   Gravado em cabana.txt
#
# REQUISITOS
# ----------
# [ ] Usa open() com modo "w"
# [ ] Usa .write()
# [ ] Fecha o arquivo com .close()
#
# DICA
# ----
# O modo "w" sobrescreve o arquivo se ele ja existir. Pra escrever em varias
# linhas, inclua "\n" no fim de cada uma.
#
# VALIDACAO
# ---------
# Depois de rodar, o arquivo cabana.txt existe e contem a mensagem digitada.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
