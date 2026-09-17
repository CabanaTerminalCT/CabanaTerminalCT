# =============================================================================
# 057 - Muitos argumentos
# Nivel: 4 estrelas
# Conceitos: *args, **kwargs
# =============================================================================
#
# HISTORIA
# --------
# O placar da CabanaTerminal as vezes soma 2 pontos, as vezes 10, as vezes uma
# lista inteira. Em vez de criar mil funcoes, a gente usa *args pra aceitar
# quantos argumentos vierem.
#
# TAREFA
# ------
# 1. Defina somar_tudo(*args) que retorna a soma de todos os numeros passados
# 2. Teste com 2, 3 e 5 argumentos
# 3. Defina mostrar_ficha(**kwargs) que imprime cada chave e valor
# 4. Chame mostrar_ficha(nome="ana", pontos=42)
#
# Exemplo de execucao:
#
#   $ python3 057_muitos_argumentos.py
#   Soma 2: 3
#   Soma 3: 6
#   Soma 5: 15
#   nome = ana
#   pontos = 42
#
# REQUISITOS
# ----------
# [ ] Usa *args numa funcao
# [ ] Usa **kwargs em outra
# [ ] Percorre os dois
#
# DICA
# ----
# - *args vira uma tupla: pode somar com sum(args).
# - **kwargs vira um dict: percorra com .items().
#
# VALIDACAO
# ---------
# somar_tudo(1,2) -> 3; somar_tudo(1,2,3,4,5) -> 15; kwargs imprimem os pares.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
