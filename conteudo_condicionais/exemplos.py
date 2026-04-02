# Crie um algoritmo que peça o preço de um compra e peça o tipo de pagamento
# Se for avista ou pix dê 12% de desconto no valor da compra
# Imprima: total da compra, valor do desconto aplicado e o valor final.

# compra = float(input('Digite o valor da compra: '))
# tipo_pagamento = input('Digite o tipo de pagamento (A - Avista | P - PIX | C - Crédito | D - Débito): ').upper()
# desconto = 0
# if tipo_pagamento == 'A' or tipo_pagamento == 'P':
#     desconto = compra * 0.12

# compra_final = compra - desconto

# print('Valor da compra', compra)
# print('Desconto', desconto)
# print('Valor final', compra_final)

# Crie um algoritmo que peça idade, quantidade de saldo e cartão VIP
# Se a (idade for maior que 25 E o saldo for maior que 1000) OU possui cartão VIP
# Imprima: Bem-vindo, aceita um café?
# Se não, imprima: Caia fora malandrão.

# idade = int(input('Digite a idade: '))
# saldo = float(input('Digite o seu saldo: '))
# vip = input('Possui cartão VIP? (S / N)').upper()

# if idade > 25 and saldo > 1000 or vip == 'S':
#     print('Bem-vindo, aceita um café?')
# else:
#     print('Caia fora malandrão')

# Obtenha o HP total do jogador e um valor de dano
# Se o valor de dano corresponder a 50% do HP total aplique um dano extra de +20
# Imprima o HP final do jogador.

# Ex1: HP: 100 | Dano: 50 | 100 - 70 = 30
# Ex2: HP: 100 | Dano: 40 | 100 - 40 = 60

pontoVida = int(input('Digite seus pontos de vida: '))
dano = int(input('Quanto de dano você tomou? '))

metade = pontoVida / 2
if dano == metade:
    dano = dano + 20
print(f'Seu HP final é {pontoVida - dano}')

# Você foi teletransportado para o mundo do GTA 6 e precisa roubar um carro
# Obtenha as informações: Você possui a chave do veículo? Você é malandro? Você tem coragem?
# Se possui a chave OR é malandro E tem coragem
# Imprima: "O carro é meu!" Se não, "SE FUDEU"

# p1 = input('Você possui a chave do veículo?')
# p2 = input('Você é malandro?')
# p3 = input('Você tem coragem?')
# if p1 == 'S' or p2 == 'S' and p3 == 'S':
#     print('O carro é meu!')
# else:
#     print('SE FUDEU')