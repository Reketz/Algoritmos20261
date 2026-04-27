while True:
    continuar = input('Deseja continuar? (S/N)')
    if continuar == 'S':
        print('ok, vou parar...')
        break

# crie uma calculado usando while e break
# operações: somar, subtrair, dividir e multiplicar 
# continue perguntando se o usuário quer continuar
# com a operação... 

while True:
    opr = input('+ - / *')
    if opr == "=":
        break
    if opr == "+":
        while True:
            num1 = float(input('numero 1: '))
            num2 = float(input('numero 2: '))
            print('Soma', num1 + num2)
            continuar = input('Continua? (S / N)')
            if continuar == "N":
                break


# Faça uma conta bancária com as operações
# Consultar saldo, sacar, depositar, extrato, emprestimo
# Só saca se tiver saldo
# Só deposita se for valor positivo
# O extrato deve mostrar em texto as entradas e saídas...
