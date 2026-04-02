# comeco = input('Deseja começar? (S/N)')
# while comeco == 'S':
#     print('começou')

# contador = 10
# while contador >= 1:
#     print('numero' , contador)
#     contador -= 1

# qtdNumero = int(input('digite a quatnidade de numeros: '))
# resultado = 0
# while qtdNumero > 0:
#     numero = int(input('Digite o número: '))
#     operacao = input('Operaçao: (+ -) ')
#     if operacao == "+":
#         resultado += numero
#     elif operacao == "-":
#         resultado -= numero

#     qtdNumero -= 1

# print('Soma', resultado)



# entrada = input('Deseja entrar na balada? (S/N)')
# homens = 0
# mulheres = 0
# while entrada == 'S':
#     idade = int(input('Digite a sua idade: '))
#     if idade >= 18:
#         sexo = input('Digite seu sexo: (M - Masculino | F - Femino)')
#         if sexo == "M":
#             homens += 1
#         elif sexo == "F":
#             mulheres += 1
#     else:
#         print('Você não tem idade pra entrar, va dormir')

#     entrada = input('Deseja entrar na balada? (S/N)')

# print('Homens', homens)
# print('Mulheres', mulheres)
# print('Pessoas', homens + mulheres)

entrada = int(input('Tem quantas pessoas na fila?'))
homens = 0
mulheres = 0
menores = 0
naoidentificado = 0
while entrada > 0:
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        entrada -= 1
        sexo = input('Digite seu sexo: (M - Masculino | F - Femino)')
        if sexo == "M":
            homens += 1
        elif sexo == "F":
            mulheres += 1
        else:
            naoidentificado += 1
    else:
        menores += 1
        print('Você não tem idade pra entrar, va dormir')

print('Homens', homens)
print('Mulheres', mulheres)
print('Pessoas', homens + mulheres)