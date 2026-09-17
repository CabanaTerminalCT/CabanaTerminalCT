# =============================================================================
# 024 - Limpa o excesso
# Nivel: 2 estrelas
# Conceitos: .strip(), .lstrip(), .rstrip()
# =============================================================================
#
# HISTORIA
# --------
# Usuario digita " cabana  " com espacos sobrando e o programa da
# CabanaTerminal nao reconhece. Acontece todo dia. A solucao e limpar as
# bordas da string antes de usar.
#
# TAREFA
# ------
# 1. Peca um texto ao usuario (com espacos, se quiser)
# 2. Mostre o tamanho original
# 3. Mostre o tamanho depois do .strip()
# 4. Mostre o texto limpo entre colchetes pra provar
#
# Exemplo de execucao:
#
#   $ python3 024_limpa_o_excesso.py
#   Texto:    cabana
#   Original: 10
#   Limpo: 6
#   Resultado: [cabana]
#
# REQUISITOS
# ----------
# [ ] Usa len() antes e depois
# [ ] Usa .strip()
# [ ] Mostra o resultado entre colchetes
#
# DICA
# ----
# .strip() tira espacos das duas pontas. .lstrip() so da esquerda e .rstrip()
# so da direita. Nenhum deles mexe no meio do texto.
#
# VALIDACAO
# ---------
# "  cabana  " -> 10 antes, 6 depois.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
