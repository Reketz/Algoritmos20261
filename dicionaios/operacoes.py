# pessoa = {
#     "ativo": True,
#     "nome": "Paulo",
#     "idade": 29,
#     "filhos": [
#         {"nome": "João", "idade": 6}, 
#         {"nome": "Maria", "idade": 9}
#     ],
#     "identidade": {
#         "cpf": 1235467846,
#         "rg": 3222331
#     },
#     "saldoDaConta": -10.0
# }

# capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
# pais = input('Digite um país: ')
# capital_brasil = capitais[pais]
# print(capital_brasil)

# capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
# pais = "Itália"
# if pais in capitais:
#     capital = capitais[pais]
#     print(f"A capital de {pais} é {capital}.")
# else:
#     print(f"A capital de {pais} não foi encontrada no dicionário!")

# capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
# capitais["Itália"] = "Roma"# Cria uma nova chave:valor

# capital_italia = capitais["Itália"]
# print(capital_italia)

# usuario = {
#     "usuario": "admin",
#     "senha": "123@321"
# }
# novaSenha = input('Digite a nova senha: ')
# usuario["senha"] = novaSenha

# print(usuario)

# meu_dicionario = {"nome": "Alice", "idade": 25}
# meu_dicionario.update({"idade": 26, "cidade": "São Paulo"})
# print(meu_dicionario)

# print(meu_dicionario['nome'])
# print(meu_dicionario['idade'])
# print(meu_dicionario['cidade'])

# capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
# del capitais["Brasil"]

# print(capitais)

# capitais = {"Brasil":[ "Brasília", "Paraiba", "Ceara"], "Alemanha": "Berlim", "Japão": "Tóquio"}
# len(capitais["Brasil"])

# meu_dicionario = {"nome": "Bob", "idade": 30}
# idade = meu_dicionario.get("idade")
# print(idade)

# cidade = meu_dicionario.get("cidade", "não existe a chave cidade")
# print(cidade)

# meu_dicionario = {"nome": "Carlos", "idade": 22}
# valor_idade = meu_dicionario.pop("idade")
# print(valor_idade)
# print(meu_dicionario)

# Crie um subsistema de cadastro de produto com 2 opções
# 1 - cadastrar produto (nome, quantidade, preço de venda)
# 2 - listar produtos
# Use listas com dicionários!