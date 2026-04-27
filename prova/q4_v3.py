s = int(input('Valor: '))
centenas = s // 100
resto = s % 100
dezenas = resto // 10
unidades = resto % 10

print(centenas)
print(dezenas)
print(unidades)