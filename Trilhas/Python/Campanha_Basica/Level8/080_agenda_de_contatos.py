# =============================================================================
# 080 - Mini-projeto: agenda de contatos
# Nivel: 4 estrelas
# Conceitos: arquivos, json, funcoes, menu
# =============================================================================
#
# HISTORIA
# --------
# A CabanaTerminal quer uma agenda de contatos que NAO perca os dados ao
# fechar. Tudo fica salvo num JSON e recarregado ao abrir. Este mini-projeto
# fecha o capitulo de persistencia.
#
# TAREFA
# ------
# 1. Ao iniciar, carregue os contatos de "contatos.json" (se existir)
# 2. Menu em loop:
#      [1] adicionar contato (nome + telefone)
#      [2] listar contatos
#      [3] buscar por nome
#      [4] remover contato
#      [sair] salvar e sair
# 3. Salve tudo em JSON ao sair
# 4. Trate arquivo inexistente e entrada invalida
#
# Exemplo de execucao:
#
#   $ python3 080_agenda_de_contatos.py
#   [1] add  [2] listar  [3] buscar  [4] remover  [sair]
#   Opcao: 1
#   Nome: ana
#   Telefone: 1234
#   Contato salvo!
#   ...
#   Opcao: sair
#   Contatos salvos em contatos.json
#
# REQUISITOS
# ----------
# [ ] Carrega JSON no inicio (com padrao se nao existir)
# [ ] Salva JSON no fim
# [ ] Funcoes separadas pra cada acao
# [ ] Menu com while e tratamento de erro
#
# DICAS
# -----
# - Use um dict {nome: telefone} pros contatos.
# - Envolva o carregamento num try/except FileNotFoundError.
# - Use json.dump(..., indent=2, ensure_ascii=False) pra salvar legivel.
#
# VALIDACAO
# ---------
# Adicione contatos, saia, rode de novo: os contatos continuam la. Buscar e
# remover funcionam.
#
# Terminou? Voce fechou o Capitulo 8. [root@cabana]# exit
# =============================================================================


# >>> SEU CODIGO AQUI <<<
