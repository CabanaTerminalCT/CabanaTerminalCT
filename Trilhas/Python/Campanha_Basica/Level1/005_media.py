# =============================================================================
# 005 - Media de 3 notas
# Nivel: 1 estrela
# Conceitos: int/float, divisao /
# =============================================================================
#
# HISTORIA
# --------
# Na CabanaTerminal ninguem e avaliado por diploma, mas quem participa das
# trilhas recebe uma nota de esforco. Seu papel e calcular a media de tres
# notas.
#
# TAREFA
# ------
# 1. Peca tres notas ao usuario (podem ter casas decimais)
# 2. Calcule a media
# 3. Mostre a media na tela
#
# Exemplo de execucao:
#
#   $ python3 005_media.py
#   Nota 1: 7
#   Nota 2: 8.5
#   Nota 3: 9
#   Media: 8.166666666666666
#
# REQUISITOS
# ----------
# [ ] Le as tres notas com input()
# [ ] Converte para float() (aceita decimais)
# [ ] Usa / para dividir por 3
# [ ] Mostra a media
#
# DICA
# ----
# float("8.5") funciona; int("8.5") quebra com ValueError. Para notas, use
# float. Quer arredondar? round(media, 2) deixa com 2 casas.
#
# VALIDACAO
# ---------
# Notas 7, 8.5 e 9 -> media 8.166... Com round(..., 2) -> 8.17.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
