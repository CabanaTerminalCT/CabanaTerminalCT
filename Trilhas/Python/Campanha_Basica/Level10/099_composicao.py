# =============================================================================
# 099 - Composicao
# Nivel: 4 estrelas
# Conceitos: objeto dentro de objeto
# =============================================================================
#
# HISTORIA
# --------
# Nem tudo se resolve com heranca. Um membro da CabanaTerminal TEM um
# endereco, TEM uma mochila. Isso e composicao: um objeto guardando outros
# objetos. Muitas vezes e melhor que herdar.
#
# TAREFA
# ------
# 1. Crie a classe Endereco(cidade, estado)
# 2. Crie a classe Membro(nome, endereco) que guarda um objeto Endereco
# 3. Crie um Endereco e passe pro Membro
# 4. Mostre a cidade do membro acessando membro.endereco.cidade
#
# Exemplo de execucao:
#
#   $ python3 099_composicao.py
#   ana mora em Recife - PE
#
# REQUISITOS
# ----------
# [ ] Uma classe guarda uma instancia de outra
# [ ] Acessa atributo aninhado (objeto.atributo_objeto.atributo)
# [ ] Comenta a diferenca entre heranca (e um) e composicao (tem um)
#
# DICA
# ----
# Heranca: Mentor E UM Membro. Composicao: Membro TEM UM Endereco. Prefira
# composicao quando a relacao for "tem".
#
# VALIDACAO
# ---------
# A cidade e o estado aparecem acessando via o objeto endereco.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
