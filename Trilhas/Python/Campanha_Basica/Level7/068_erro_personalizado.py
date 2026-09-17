# =============================================================================
# 068 - Erro personalizado
# Nivel: 4 estrelas
# Conceitos: Exception customizada
# =============================================================================
#
# HISTORIA
# --------
# ValueError e generico demais. A CabanaTerminal merece um erro com a sua
# cara: SenhaFracaError, por exemplo. Criar excecoes proprias deixa o codigo
# mais expressivo e facil de tratar.
#
# TAREFA
# ------
# 1. Crie uma classe SenhaFracaError herdando de Exception
# 2. Defina validar_senha(senha) que dispara SenhaFracaError se len < 8
# 3. Chame dentro de try/except capturando SenhaFracaError especificamente
# 4. Mostre a mensagem do erro
#
# Exemplo de execucao:
#
#   $ python3 068_erro_personalizado.py
#   Senha: abc
#   SenhaFracaError: senha muito curta
#   Senha: cabana#2026
#   Senha aceita!
#
# REQUISITOS
# ----------
# [ ] Cria classe herdando de Exception
# [ ] Usa raise com a excecao propria
# [ ] Captura a excecao propria no except
#
# DICA
# ----
# class SenhaFracaError(Exception): passa. Depois e so raise
# SenhaFracaError("senha muito curta") e except SenhaFracaError as e.
#
# VALIDACAO
# ---------
# "abc" dispara SenhaFracaError; "cabana#2026" e aceita.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
