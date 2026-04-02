saque = int(input('Digite o valor do saque: '))

if saque >= 10 and saque <= 600:
    if saque >= 100:
        notas = saque // 100
        print(notas, 'notas de cem')
        saque = saque - (notas * 100)
    if saque >= 50:
        notas = saque // 50
        print(notas, 'notas de cinquenta')
        saque = saque - (notas * 50)
    if saque >= 10:
        notas = saque // 10
        print(notas, 'notas de dez')
        saque = saque - (notas * 10)
    if saque >= 5:
        notas = saque // 5
        print(notas, 'notas de cinco')
        saque = saque - (notas * 5)
    if saque >= 1:
        notas = saque // 1
        print(notas, 'notas de um')
        saque = saque - (notas * 1)
else:
    print('Somente valores minimos de 10 e maximos de 600')