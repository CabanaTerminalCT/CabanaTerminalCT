# =============================================================================
# 069 - Nao engole erro
# Nivel: 4 estrelas
# Conceitos: evitar except: pass
# =============================================================================
#
# HISTORIA
# --------
# Tem um anti-padrao que assombra a CabanaTerminal: "except: pass". O programa
# parece funcionar, mas esconde o erro e voce fica horas sem saber o que
# quebrou. Este desafio e sobre tratar erro com responsabilidade.
#
# TAREFA
# ------
# 1. Escreva uma funcao dividir(a, b) que trata ZeroDivisionError de forma
#    explicita, retornando None e AVISANDO no terminal
# 2. Escreva uma versao "ruim" (comentada) que usa except: pass e explique em
#    comentario por que ela e perigosa
# 3. No programa principal, chame dividir(10, 0) e dividir(10, 2) e mostre que
#    o erro foi tratado de forma visivel
#
# Exemplo de execucao:
#
#   $ python3 069_nao_engole_erro.py
#   [AVISO] nao da pra dividir por zero
#   Resultado: None
#   Resultado: 5.0
#
# REQUISITOS
# ----------
# [ ] Trata o erro de forma explicita (sem pass silencioso)
# [ ] Comenta o anti-padrao except: pass
# [ ] Deixa o aviso visivel ao usuario
#
# DICA
# ----
# except: pass engole QUALQUER erro - ate erros de programacao que voce
# deveria ver. Prefira capturar o tipo especifico e sempre dar um retorno
# (log, mensagem, valor padrao).
#
# VALIDACAO
# ---------
# dividir(10,0) avisa e devolve None; dividir(10,2) devolve 5.0.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
