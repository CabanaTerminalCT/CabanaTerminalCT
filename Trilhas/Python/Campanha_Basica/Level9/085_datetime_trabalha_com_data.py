# =============================================================================
# 085 - Datetime: trabalha com data
# Nivel: 4 estrelas
# Conceitos: datetime
# =============================================================================
#
# HISTORIA
# --------
# O log da CabanaTerminal precisa de carimbo de tempo, e o cadastro precisa
# calcular idade. O modulo datetime resolve data e hora sem voce quebrar a
# cabeca com fuso e formato.
#
# TAREFA
# ------
# 1. Mostre a data e hora atuais
# 2. Formate a data no padrao "dd/mm/aaaa HH:MM"
# 3. Peca uma data de nascimento (ano) e calcule a idade
# 4. Mostre quantos dias faltam pro fim do ano (aproximado)
#
# Exemplo de execucao:
#
#   $ python3 085_datetime_trabalha_com_data.py
#   Agora: 17/09/2026 14:30
#   Ano de nascimento: 2000
#   Idade: 26
#   Faltam ~105 dias pro fim do ano
#
# REQUISITOS
# ----------
# [ ] Importa datetime
# [ ] Usa datetime.now()
# [ ] Usa strftime pra formatar
# [ ] Calcula a idade com o ano atual
#
# DICA
# ----
# datetime.now() da o momento atual. .strftime("%d/%m/%Y %H:%M") formata.
# .year da so o ano. Pra idade: ano_atual - ano_nascimento (aproximado).
#
# VALIDACAO
# ---------
# A data sai formatada; a idade bate com o ano atual.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
