# =============================================================================
# 108 - Testa manualmente
# Nivel: 4 estrelas
# Conceitos: QA, casos de teste
# =============================================================================
#
# HISTORIA
# --------
# Antes de subir o projeto pra CabanaTerminal, a gente testa. Nao precisa de
# framework ainda - um bom roteiro manual de casos de teste ja pega 90% dos
# bugs.
#
# TAREFA
# ------
# 1. Monte uma lista de casos de teste pro seu projeto, cobrindo:
#      - caminho feliz (tudo certo)
#      - entradas invalidas
#      - limites (vazio, zero, muito grande)
#      - persistencia (salvar e recarregar)
# 2. Escreva os casos como comentario/estrutura no arquivo
# 3. Execute cada um no seu projeto e marque passou/falhou
# 4. Corrija o que falhar
#
# Exemplo de execucao:
#
#   $ python3 108_testa_manualmente.py
#   === ROTEIRO DE TESTES ===
#   [OK] adicionar registro valido
#   [OK] rejeitar entrada invalida
#   [OK] listar vazio sem quebrar
#   [OK] dados persistem apos reiniciar
#   Resultado: 4/4
#
# REQUISITOS
# ----------
# [ ] Pelo menos 6 casos de teste listados
# [ ] Cobre caminho feliz, erro e limites
# [ ] Inclui teste de persistencia
#
# DICA
# ----
# Um caso de teste bom tem: entrada, acao e resultado esperado. "Adicionar
# 'ana' com 10 pontos deve aparecer na listagem com 10 pontos".
#
# VALIDACAO
# ---------
# O roteiro cobre os fluxos principais e voce consegue dizer quais passaram.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
