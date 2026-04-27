#questão 7

# numero = 0
# temNumeroDivisivel = "N"
# while numero >= 0:
#     numero = int(input('Número: '))
#     if numero % 10 == 0:
#         temNumeroDivisivel = "S"

# if temNumeroDivisivel == "S":
#     print('Existe multiplo de 10 nesse conjunto')
# else:
#     print('Não existe multiplo de 10 nesse conjunto')

#questão 7 - outra versão

numero = 0
temNumeroDivisivel = False
while numero >= 0:
    numero = int(input('Número: '))
    if numero % 10 == 0:
        temNumeroDivisivel = True

if temNumeroDivisivel:
    print('Existe multiplo de 10 nesse conjunto')
else:
    print('Não existe multiplo de 10 nesse conjunto')