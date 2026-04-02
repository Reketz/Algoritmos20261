# Quando usar somente if?

# Crie um algoritmo que verifique se a soma de dois números
# é maior que 10, se verdadeiro E a soma for par incremente
# +5 se não, incremente +2
# n1 = int(input('Digite o n1: '))
# n2 = int(input('Digite o n2: '))
# soma = n1 + n2

# if(soma > 10 and soma % 2 == 0):
#     soma = soma + 5
# else:
#     soma += 2

# print(soma)

# Obtem o valor de uma compra e uma forma de pagamento
# Se avista 10% de desconto 
# Se debito 5% de desconto
# Se crédito 2% de acrescimo

# compra = float(input('Digite o valor da compra: '))
# forma = input('Digite o pagamento: (A - D - C): ')
# if(forma == "A"):
#     desconto = compra * 10 / 100
#     compra -= desconto
# elif(forma == "D"):
#     desconto = compra * 5 / 100
#     compra -= desconto
# elif(forma == "C"):
#     acrescimo = compra * 2 / 100
#     compra += acrescimo

# print('Compra: ', compra)



# Crie um algoritmo para validar se uma senha é válida
# Verifique se a senha possui pelo menos 8 caracters
# Verifique se a senha possui um caractere especial: @!+-.#
# verifique se a senha é diferente de 12345678, 87654321.
senha = input('Digite sua senha: ')
contador = 0

if len(senha) >= 8:
    contador += 1

if ("@" in senha) or ("!" in senha) or ("+" in senha):
    contador += 1

if senha != "12345678" and senha != "87654321":
    contador += 1

if contador == 3:
    print('senha válida!')
else:
    print('senha inválida')





logado = "S"
tipo = "ADMIN"

if(logado == "S"):
    print('Bem vindo, usuário!')

    if(tipo == "ADMIN"):
        print('Tem acesso')
        senha = input('senha:')
        if senha == "admin123":
            print('liberar o recurso')
        else:
            print('senha invlaida')
    else:
        print('Acesso negado')
