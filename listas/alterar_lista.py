frutas = ['banana', 'uva', 'maçã']

# substituir = input('Digite a fruta para substituir: ')
# novaFruta = input('Digite o nome da nova fruta: ')
apagar = input('Digite o nome da fruta para remover: ')
for posicao in range(len(frutas)):# 0 1 2
    if frutas[posicao] == apagar:
        frutas.pop(posicao)
        break

# print(frutas)
