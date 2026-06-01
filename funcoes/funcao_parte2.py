import random
for i in range(50):
    print(random.random())

# def inputValorPositivo(mensagem):
#     valor = input(mensagem)
#     while not valor.isdigit():
#         print('Valor inválido, digite um valor numérico!')
#         valor = input(mensagem)
    
#     valor = float(valor)
#     while valor <= 0:
#         print('Valor deve ser maior que 0, digite novamente!')
#         valor = input(mensagem)
#         if not valor.isdigit():
#             valor = 0

#     return valor

# quantidade = inputValorPositivo('Digite a quantidade: ')
# preco = inputValorPositivo('Digite o preço: ')

# def cadastrarAnimal(identificacao, peso, status, preco):
#     # código que faz o add na lista
#     print('Animal adicionado!')

# cadastrarAnimal(status="Em lactação", identificacao=1, peso=10, preco=511)
# cadastrarAnimal(1, 10, 'Em lactação', 511)