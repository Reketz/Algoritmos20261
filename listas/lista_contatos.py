# Criar um contato novo
# Alterar um contato existente
# Buscar um contato existente
# Apagar um contato existente

# número do telefone
contatos = [
    ['Guilherme', '83998945625', 'guilherme@email.com'],
    ['Henrique', '839989454546', 'a@email.com'],
    ['Jonnata', '83998945625', 'b@email.com'],
    ['Joao', '89465321321', 'c@email.com'],
    ['Pedro', '54445466454', 'd@email.com']
]

while True:
    print('Bem vindo a ContactPython App')
    print('1 - Criar contato')
    print('2 - Buscar contato por nome')
    print('3 - Listar contatos')
    print('4 - Alterar contato')
    print('5 - Apagar contato')
    print('6 - Buscar contato por celular')
    print('0 - Sair')
    opcao = int(input('Digite a opção: '))
    if opcao == 0:
        break
    elif opcao == 1:
        nome = input('Digite o nome do contato: ')
        celular = input('Digite o celular: ')
        email = input('Digite o email: ')
        contatos.append([nome, celular, email])
    elif opcao == 2:
        print('-' * 50)
        nome = input('Digite o nome do contato: ')
        for c in contatos:
            if c[0] == nome:
                print(c[0], ' | ', c[1], ' | ', c[2]) 
        print('-' * 50)
    elif opcao == 3:
        print('-' * 50)
        for c in contatos:
            print(c[0], ' - ', c[1], ' - ', c[2])

        print('-' * 50)
    elif opcao == 4:
        print('Para alterar informe o dado abaixo')
        celular = input('Digite o celular do contato: ')
        for posicao in range(len(contatos)):
            if contatos[posicao][1] == celular:
                nome = input('Digite o novo nome: ')
                celular = input('Digite o novo celular: ')
                email = input('Digite o novo email: ')
                contatos[posicao] = [nome, celular, email]
                print('\n\nContato alterado com sucesso!\n\n')
    elif opcao == 5:
        print('Para apagar informe o dado abaixo')
        celular = input('Digite o celular do contato que deseja apagar: ')
        
        for posicao in range(len(contatos)):
            if contatos[posicao][1] == celular:
                contatos.pop
                print('contato removido com sucesso!')
                break
    elif opcao == 6:
        print('-' * 50)
        celular = input('Digite o celular do contato: ')
        for c in contatos:
            if c[1] == celular:
                print(c[0], ' | ', c[1], ' | ', c[2]) 
        print('-' * 50)