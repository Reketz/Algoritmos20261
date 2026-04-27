s = int(input('Valor: '))
if s >= 10 and s<= 600:
    n1 = s // 100
    resto = (s % 100) % 50
if resto < 100:
    n2 = s // 50
    resto = (s % 50) % 10
if resto < 100:
    n3 = s // 10
    resto = (s % 10) % 5
if resto < 100:
    n4 = s // 5
    resto = (s % 5) % 1

print(f'{n1} notas de 100')
print(f'{n2} notas de 50')
print(f'{n3} notas de 10')
print(f'{n4} notas de 5')