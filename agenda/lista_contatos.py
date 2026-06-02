# Criar um contato novo
# Alterar um contato existente
# Buscar um contato existente
# Apagar um contato existente

# número do telefone
caminho = "C:/Users/Guilherme/Documents/FACULDADE/ALGORITMOS/Algoritmos20261/arquivos/agenda.txt"

contatos = [
    # {'nome': 'Guilherme', 'telefone': '83998945625', 'email': 'guilherme@email.com'},
    # {'nome': 'Henrique', 'telefone': '839989454546', 'email': 'a@email.com'},
    # {'nome': 'Jonnata', 'telefone': '83998945625', 'email': 'b@email.com'},
    # {'nome': 'Joao', 'telefone': '89465321321', 'email': 'c@email.com'},
    # {'nome': 'Pedro', 'telefone': '54445466454', 'email': 'd@email.com'}
]

# funções da lista de contatos
def cadastrarContato():
    nome = input('Digite o nome do contato: ')
    celular = input('Digite o celular: ')
    email = input('Digite o email: ')
    c = {"nome": nome,"telefone": celular, "email":email}
    contatos.append(c)

def buscarContatoPorNome(nome):
    print('-' * 50)
    for c in contatos:
        if c['nome'] == nome:
            print(c['nome'], ' | ', c['telefone'], ' | ', c['email']) 
    print('-' * 50)

def buscarContatoPorCelular(celular):
    print('-' * 50)
    for c in contatos:
        if c['telefone'] == celular:
            print(c['nome'], ' | ', c['telefone'], ' | ', c['email']) 
    print('-' * 50)

def listarContatos():
    print('-' * 50)
    for c in contatos:
        print(c['nome'], ' | ', c['telefone'], ' | ', c['email']) 
    print('-' * 50)

def alterarContato(celular):
    print('Para alterar informe o dado abaixo')
    for posicao in range(len(contatos)):
        if contatos[posicao]['telefone'] == celular:
            nome = input('Digite o novo nome: ')
            celular = input('Digite o novo celular: ')
            email = input('Digite o novo email: ')
            c = {"nome": nome,"telefone": celular, "email":email}
    
            contatos[posicao] = c
            print('\n\nContato alterado com sucesso!\n\n')

def apagarContato(celular):
    for posicao in range(len(contatos)):
        if contatos[posicao]['telefone'] == celular:
            contatos.pop(posicao)
            print('contato removido com sucesso!')
            break


def salvarArquivo():
    with open(caminho, "a") as arq:
        for c in contatos:
            arq.write(f'{c["nome"]},{c["telefone"]},{c["email"]}\n')
def iniciarArquivo():
     with open(caminho, "r") as arquivo:
        conteudo = arquivo.readlines()
        for c in conteudo:
            c.replace('\n', '')
            dados = c.split(',')
            nome = dados[0]
            telefone = dados[1]
            email = dados[2]
            contatos.append({
                "nome": nome,
                "telefone": telefone,
                "email":email
            })

def iniciarMenu():
    print('Bem vindo a ContactPython App')
    print('1 - Criar contato')
    print('2 - Buscar contato por nome')
    print('3 - Listar contatos')
    print('4 - Alterar contato')
    print('5 - Apagar contato')
    print('6 - Buscar contato por celular')
    print('0 - Sair')
   
while True:
    iniciarMenu()
    if(len(contatos) == 0):
        iniciarArquivo()
    opcao = int(input('Digite a opção: '))
    if opcao == 0:
        salvarArquivo()
        break
    elif opcao == 1:
        cadastrarContato()
    elif opcao == 2:
        nome = input('Digite o nome do contato: ')
        buscarContatoPorNome(nome)
    elif opcao == 3:
        listarContatos()
    elif opcao == 4:
        celular = input('Digite o celular do contato: ')
        alterarContato(celular)
    elif opcao == 5:
        print('Para apagar informe o dado abaixo')
        celular = input('Digite o celular do contato que deseja apagar: ')
        apagarContato(celular)
    elif opcao == 6:
        celular = input('Digite o celular do contato: ')
        buscarContatoPorCelular(celular)