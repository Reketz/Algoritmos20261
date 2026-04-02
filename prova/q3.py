numParticipantes = int(input('Participantes: '))
valorMatricula = numParticipantes * 44

if numParticipantes >= 5:
    desconto = valorMatricula * 10 / 100
    valorMatricula = valorMatricula - desconto

print(valorMatricula)