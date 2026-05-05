# time1 = {"ashe", "pikachu"}
# time2 = {"bulbasaur", "pidgey", "pikachu"}

# print(time1.union(time2))

# produtos = [ [ "maça", 10 ], ["banana", 25 ] ]

# produtos[0][1] = produtos[0][1] + 5

# print(produtos)

# nome = input('DIgite o pokemon: ').lower()
# pokemons = { "pikachu" , nome }
# print(pokemons)


tipo = input('Tipo 1 - ADM 2 - CLIENTE: ')

if tipo.isdigit():
    tipo = int(tipo)
    if tipo != 1 or tipo != 2:
        print('TIpo inválido')
else:
    print('Tipo inválido')

