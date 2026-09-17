# =============================================================================
# 066 - Cria teu erro
# Nivel: 4 estrelas
# Conceitos: raise
# =============================================================================
#
# HISTORIA
# --------
# Nem todo erro vem do Python. As vezes a regra e da CabanaTerminal: idade
# negativa, nick vazio, pontos fora do limite. Voce mesmo dispara o erro com
# raise pra deixar claro que aquele valor e invalido.
#
# TAREFA
# ------
# 1. Defina validar_idade(idade) que:
#      - dispara raise ValueError se idade < 0
#      - dispara raise ValueError se idade > 150
#      - retorna "ok" se estiver valida
# 2. Chame dentro de um try/except e mostre a mensagem do erro
#
# Exemplo de execucao:
#
#   $ python3 066_cria_teu_erro.py
#   Idade -5: Idade invalida: -5
#   Idade 200: Idade invalida: 200
#   Idade 30: ok
#
# REQUISITOS
# ----------
# [ ] Usa raise
# [ ] Dispara ValueError com mensagem propria
# [ ] Trata com try/except
#
# DICA
# ----
# raise ValueError("Idade invalida: -5") interrompe e sobe o erro pra quem
# chamou. Quem chama pode tratar com try/except.
#
# VALIDACAO
# ---------
# -5 e 200 levantam erro com mensagem; 30 retorna "ok".
# =============================================================================


# >>> SEU CODIGO AQUI <<<
