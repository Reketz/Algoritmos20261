# qtdPessoas = int(input('Quantas pessoas tem na fila?'))
# homens = 0
# mulheres = 0
# menores = 0
# naoidentificado = 0
# for i in range(qtdPessoas):
#     idade = int(input('Digite a sua idade: '))
#     if idade >= 18:
#         sexo = input('Digite seu sexo: (M - Masculino | F - Femino)')
#         if sexo == "M":
#             homens += 1
#         elif sexo == "F":
#             mulheres += 1
#         else:
#             naoidentificado += 1
#     else:
#         menores += 1
#         print('Você não tem idade pra entrar, va dormir')

# print('Homens', homens)
# print('Mulheres', mulheres)
# print('Pessoas', homens + mulheres)

# for i in range(5):
#     senha = input('Digite a senha: ')
#     if senha != "a1d2m3i4n5":
#         print('Digite novamente!!')
#     else:
#         print('Acertou mizera')
#         break

# usando "for"
# pede 10 numeros pro usuário e faz o somatorio e a média
# soma = 0
# for i in range(20):
#     numero = float(input('Digite um numero agora ligeiro: '))
#     soma = soma + numero

# media = soma / 20
# print(soma)
# print(media)

# peça ao usuário um número de voltas que um carro percorre
# em uma pista. Para cada volta pergunte ao usuário quanto
# tempo ele gastou na volta
# imprima o menor tempo digitado...

# voltas = int(input('Digite o numero de voltas: ')) 
# menor =  int(input('Digite o tempo da volta: '))
# print('Volta atual é 1 com tempo', menor)

# for i in range(voltas-1):
#     tempo = int(input('Digite o tempo da volta: '))
#     if tempo < menor:
#         menor = tempo
#     print('Volta atual é', i+2, 'com tempo', tempo)

# print(f'o menor tempo percorrido foi de {menor}')

# for i in range(10):
#     print(i)
nome = input('digite o seu nome:')
for letra in nome:
    print(letra)