qtd = int(input('Digite a quantidade de kWh: '))
bandeira = input('Digite a bandeira: ')

if qtd <= 100:
    valorBase = qtd * 0.5
elif qtd > 100 and qtd <= 200:
    valorBase = qtd * 0.7
elif qtd > 200:
    valorBase = qtd * 0.9

if bandeira == "verde":
    print('Sem acrescimo')
elif bandeira == "amarelo":
    acrescimo = valorBase * 15 / 100
    valorBase = valorBase + acrescimo
elif bandeira == "vermelho":
    acrescimo = valorBase * 22 / 100
    valorBase = valorBase + acrescimo

print('Total da conta: ', valorBase)