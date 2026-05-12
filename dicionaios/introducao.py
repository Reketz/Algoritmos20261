
# posicao = [0        1         2             3]
# produtos = ["Queijo", "Leite", "Milho", "Cana de açucar"]

produtos = [
    {
        "nome": "Queijo",
        "preco": 10.89,
        "saldo": 10
    },
    {
        "nome": "Leite",
        "preco": 7.56,
        "saldo": 30
    },
    {
        "nome": "Milho",
        "preco": 15.4,
        "saldo": 100
    }
]
total = 0
for prod in produtos:
    somatorio = prod['preco'] * prod['saldo']
    total += somatorio
    print(f'{prod['nome']} | {prod['preco']} x {prod['saldo']} = {somatorio}')

print('Seu total de estoque é:', total)

produtos = {
    "78935132": ["Queijo", 10.5, 100]
}

produtos["78935132"]