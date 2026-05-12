# time1 = {"ashe", "pikachu"}
# time2 = {"bulbasaur", "pidgey", "pikachu"}

# print(time1.union(time2))

# produtos = [ [ "maça", 10 ], ["banana", 25 ] ]

# produtos[0][1] = produtos[0][1] + 5

# print(produtos)

# nome = input('DIgite o pokemon: ').lower()
# pokemons = { "pikachu" , nome }
# print(pokemons)


data = input('Data: (dd/mm/aaaa) ')
while len(data) != 10 or "/" not in data:
    print('Data inválida')
    data = input('Data: (dd/mm/aaaa) ')

dataFormatada = data.split('/')
dia = dataFormatada[0]
mes = dataFormatada[1]
ano = dataFormatada[2]

print(dia)
print(mes)
print(ano)

# nomes = 'gabriel,bruno,alice,ana'
# lista = nomes.split(',')
# print(lista[0])