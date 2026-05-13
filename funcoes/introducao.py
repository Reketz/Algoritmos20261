# algo = input("Digite algo: ")



# def imprimirBoasVindas():
#     nome = input('Digite seu nome: ')
#     print('Bem vindo!', nome)


# imprimirBoasVindas()
# dinossauros = []

# def cadastrarDinossauro():
#     nome = input('Digite o nome do dinossauro: ')
#     altura = float(input('Digite a altura: '))
#     dinossauros.append([nome, altura])

# def listarDinossauros():
#     print('-' * 50)
#     for d in dinossauros:
#         print('Nome', d[0], 'Altura', d[1])
#     print('-' * 50)
#     print('\n\n')

# def startMenu():
#     while True:
#         print('Bem vindo ao sistema extrablaster')
#         print('1 - Adicionar dinossauro')
#         print('2 - listar dinossauros')
#         print('3 - alterar dinossauro')
#         print('4 - excluir dinossauro')
#         print('0 - Exit')
#         op = input('Digite a opção')
#         if(op == "0"):
#             break
#         elif(op == "1"):
#             cadastrarDinossauro()
#         elif(op == "2"):
#             listarDinossauros()
#         elif(op == "3"):
#             listarDinossauros()
#             dinossauro = input('Qual dinossauro você deseja alterar: ')
#             # continua com o algoritmo de alterar
#         elif(op == "4"):
#             listarDinossauros()
#             dinossauro = input('Qual dinossauro você deseja excluir: ')
#             # continua com o algoritmo de excluir
#         else:
#             print('Opção inválida')

# startMenu()

# def boasVindas(nome):
#     print('Bem vindo', nome)

# textoDigitado = input('Digite seu nome')
# boasVindas(textoDigitado)

# def somar(num1, num2):
#     print(num1 + num2)

# somar(10, 5)

# def imc(peso, altura):
#     imc = peso / (altura * altura)
#     print(imc)

# imc(50, 1.60)

# numeros = [1,5,8,5]
# soma = sum(numeros)
# print(soma)

# def sum(list):
#     if not any(list):
#         return 0
#     total = 0
#     for i in list:
#         total += i
#     return total

# numeros = [1,5,8,9]
# soma = sum(numeros)
# print(soma)

# def validarEmail(email):
#     if '@' in email and 'gmail.com' in email:
#         return True
#     else:
#         return False

# # menu de administrador
# isValido = validarEmail('guilherme@gmail.com')
# if(isValido):
#     print('Bem vindo seu perfil é adminstrador')
# else:
#     print('Não é um email válido! Entre com um email de adminstrador')

# # menu de cliente
# isValido = validarEmail('guilherme@gmail.com')
# if(isValido):
#     print('Bem vindo! Usuário')
# else:
#     print('Não é um email válido! Entre com o adminstrador do sistema!')

