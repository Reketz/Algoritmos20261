valor = int(input('Digite o valor: '))
if valor >= 100:#256
    centenas = valor // 100
    valor = valor - centenas * 100
    print(centenas, 'nota(s) de cem')

