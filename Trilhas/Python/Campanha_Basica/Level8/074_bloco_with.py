# =============================================================================
# 074 - Bloco with
# Nivel: 3 estrelas
# Conceitos: context manager
# =============================================================================
#
# HISTORIA
# --------
# Esquecer de fechar arquivo na CabanaTerminal da dor de cabeca: dados nao
# gravados, arquivo travado. O "with" fecha automaticamente, mesmo se der
# erro no meio. E o jeito profissional de mexer com arquivos.
#
# TAREFA
# ------
# 1. Reescreva a escrita e a leitura de um arquivo usando "with open(...) as f"
# 2. Grave duas linhas
# 3. Leia e mostre o conteudo
# 4. Comente por que o with e melhor que open/close manual
#
# Exemplo de execucao:
#
#   $ python3 074_bloco_with.py
#   Gravado!
#   Conteudo:
#   primeira linha
#   segunda linha
#
# REQUISITOS
# ----------
# [ ] Usa with pra escrever
# [ ] Usa with pra ler
# [ ] Nao chama .close() manualmente
#
# DICA
# ----
# with open("x.txt", "w") as f: abre e ja agenda o fechamento. Quando o bloco
# termina (normal ou com erro), o arquivo e fechado sozinho.
#
# VALIDACAO
# ---------
# O arquivo e gravado e lido corretamente, sem nenhum .close() no codigo.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
