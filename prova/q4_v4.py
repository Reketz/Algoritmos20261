s = int(input('Valor: '))
c,d,c2,c3,u = 0,0,0,0,0
q1,q2,q3,q4,q5 = 0,0,0,0,0
if s >= 100 and s <= 600:
    q1 = s // 100
    c = q1 * 100
    s -= c
if s >= 50 and s < 100:
    q2 = s // 50
    d = q2 * 50
    s -= d
if s >= 10 and s < 50:
    q3 = s // 50
    c2 = q3 * 50
    s -= c2
if s >= 5 and s < 10:
    q4 = s // 5
    c3 = q4 * 5
    s -= c3
if s >= 1 and s < 5:
    q5 = s // 1
    u = q5 * 1
    s -= u

print(q1, ' - 100')
print(q2, ' - 50')
print(q3, ' - 10')
print(q4, ' - 5')
print(q5, ' - 1')