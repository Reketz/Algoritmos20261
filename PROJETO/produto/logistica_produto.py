

produtos = [
    {"nome": "Banana", "preco": 15.5, "saldo": 100},
    {"nome": "Maça", "preco": 15.5, "saldo": 100},
    {"nome": "Abacate", "preco": 15.5, "saldo": 100},
    {"nome": "Dinossauro", "preco": 15.5, "saldo": 100}
]

def comprar(nomeProduto, quantidade):
    for p in produtos:
        if p["nome"] == nomeProduto:
            p["saldo"] += quantidade

def vender(nomeProduto, quantidade):
    for p in produtos:
        if p["nome"] == nomeProduto:
            p["saldo"] -= quantidade

def listarProdutos():
    for p in produtos:
        print(f'{p["nome"]} - {p["preco"]} - {p["saldo"]}')