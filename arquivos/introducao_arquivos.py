caminho = "C:/Users/Guilherme/Documents/FACULDADE/ALGORITMOS/Algoritmos20261/arquivos/dados.txt"

while True:
    opc = input('1 - escrever nome\n2 - ler\n0 - sair\n\nDigite: ')
    if opc == "0":
        break
    if opc == "1":
        with open(caminho, "a") as arq:
            nome = input('Digite o seu nome: ')
            idade = input('Digite sua idade: ')
            arq.write(f'{nome},{idade}\n')
    if opc == '2':
        with open(caminho, "r") as arquivo:
            conteudo = arquivo.readlines()
            for c in conteudo:
                c.replace('\n', '')
                
                dados = c.split('|')
                nome = dados[0]
                idade = dados[1]
                print(f'nome {nome} - idade {idade}')

#r = read = ler
# with open(caminho, "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)
# w = write = escrever
# with open(caminho, "w") as arq:
#     nome = input('Digite o seu nome: ')
#     arq.write(nome + "\n")

# a = append = adicionar
# with open(caminho, "a") as arq:
#     nome = input('Digite o seu nome: ')
#     arq.write(nome + "\n")

# with open("011225/\mensagem.txt", "a") as arq:
#     arq.write(input("Digite algo: ") + "\n")

# with open("011225\\mensagem.txt", "r") as arq:
#     texto = arq.read()
#     print(texto)

# with open("mensagem.txt", "r") as arq:
#     linhas = arq.readlines()
#     print(linhas)

# with open("log.txt", "a") as arq:
#     arq.write("Novo registro adicionado.\n")

# alunos = ["Ana", "Bianca", "Carlos", "Daniel"]

# with open("011225\\alunos.txt", "w") as arq:
#     for nome in alunos:
#         arq.write(nome + "\n")

# import json

# dados = {
#     "nome": "Naruto",
#     "classe": "Ninja",
#     "nível": 42,
#     "vila": "Folha"
# }

# json_str = json.dumps(dados, indent=4)
# print(json_str)

# import json

# dados = [{
#     "titulo": "Aula de Python",
#     "alunos": 35
# },
# {
#     "titulo": "Aula de Java",
#     "alunos": 32
# },
# {
#     "titulo": "Aula de C",
#     "alunos": 30
# }]

# with open("011225\\aula.json", "w") as arq:
#     json.dump(dados, arq, indent=4)

# with open("011225\\aula.json", "r") as arq:
#     dados = json.load(arq)

# for i in dados:
#     print(i["titulo"])

# import json

# json_texto = '{"nome": "Luffy", "recompensa": 1500000000}'
# python_obj = json.loads(json_texto)

# print(python_obj["nome"])

# import json

# personagem = {
#     "nome": "Tanjiro",
#     "respiração": "Água",
#     "nível": 17,
#     "habilidades": ["Golpe da água", "Redemoinho"]
# }

# with open("tanjiro.json", "w") as arq:
#     json.dump(personagem, arq, indent=4)

# import json

# with open("tanjiro.json", "r") as arq:
#     p = json.load(arq)

# print(p["habilidades"][1])

