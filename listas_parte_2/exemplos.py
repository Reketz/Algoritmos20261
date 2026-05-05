# alunos = ["Joao", "Jose", "Jonatan", "Larissa"]

# alunos.insert(2, 'Daniel')

# alunos.extend(["Bruno", "Adrian", "Henrique"])

# print(alunos)

# receitas = [10, 12.5, 15]
# despesas = [-5, -2, -13.89]

# total = receitas + despesas

# print((total))

# total = []

# operações matemáticas
# valores = [5, 10, 15, 20, 5]
# print("Soma:", sum(valores)) # soma os valores de uma lista
# print("Maior:", max(valores)) # retorna o maior valor da lista
# print("Menor:", min(valores)) # retorna o menor valor de uma lista
# print("Quantidade:", len(valores)) # retorna o tamanho da lista
# print("Quantos:", valores.count(5)) # conta os elementos da lista

contatos = [
    "Denis Vitor Feliciano Araújo",
    "Arthur da Silva Sousa",
    "Breno Rolim Pires",
    "Emerson Soares Vieira",
    "Carlos Alberto Leite Rolim N",
    "Antônio Gilvan Vieira de Mor",
    "David Abraão Oliveira de Sá",
    "Ana Alice Ferreira Maia",
    "Adryhan Miguel de Melo Sarme",
    "Deliomar Batista Vieira",
    "Douglas Alencar Pereira Viei"
]

for i in range(len(contatos)):
    print('posição', i, 'valor', contatos[i])

inter1 = int(input('Digite o primeiro intervalo'))
inter2 = int(input('Digite o segundo intervalo'))

print(contatos[inter1:inter2])