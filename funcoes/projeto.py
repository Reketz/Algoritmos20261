from funcoes.animal.funcoes_animal import cadastrarAnimal


cont = -1
users = []
logado = False

rebanho = []
estoqueProdutos = []
agendamentos = []   
historicoCompras = [] # Lista extra simples para o Tema Livre do Cliente


while cont != 0:
    print("\n================ LOGIN ================")
    print("1-Fazer login")
    print("2-Cadastrar")
    print("0-Sair")

    cont = int(input("Selecione uma opção válida: "))

    # LOGIN
    if cont == 1:
        emailUser = input("Digite seu login: ")
        senhaUser = input("Digite sua senha: ")

        encontrado = False

        for user in users:
            if emailUser == user[1] and senhaUser == user[2]:
                print("Login efetuado com sucesso!")
                logado = True
                encontrado = True

                # ================= ADM =================
                if user[3] == "administrador":
                    while logado:
                        print("\n=== MENU ADMINISTRADOR ===")
                        print("1-Gerenciar Rebanho")
                        print("2-Produção e Derivados")
                        print("3-Relatórios Detalhados (Tema Livre)")
                        print("4-Logout")

                        opAdm = int(input("Escolha: "))

                        # REBANHO
                        if opAdm == 1:
                            print("\n=== REBANHO ===")
                            print("1-Cadastrar")
                            print("2-Listar")
                            print("3-Editar")
                            print("4-Remover")
                            print("5-Buscar")

                            op = int(input("Escolha: "))

                            if op == 1:
                                cadastrarAnimal(rebanho)

                            elif op == 2:
                                if len(rebanho) == 0:
                                    print("Nenhum animal cadastrado.")
                                for animal in rebanho:
                                    print(f"Tipo: {animal[0]} | ID: {animal[1]} | Status: {animal[2]}")

                            elif op == 3:
                                idBusca = input("ID do animal para editar: ")
                                encontradoAnimal = False
                                for animal in rebanho:
                                    if animal[1] == idBusca:
                                        animal[0] = input("Novo tipo: ")
                                        animal[2] = input("Novo status: ")
                                        print("Atualizado!")
                                        encontradoAnimal = True
                                        break
                                if not encontradoAnimal:
                                    print("Animal não encontrado.")

                            elif op == 4:
                                idBusca = input("ID do animal para remover: ")
                                encontradoAnimal = False
                                for animal in rebanho:
                                    if animal[1] == idBusca:
                                        rebanho.remove(animal)
                                        print("Removido!")
                                        encontradoAnimal = True
                                        break
                                if not encontradoAnimal:
                                    print("Animal não encontrado.")

                            elif op == 5:
                                idBusca = input("ID para buscar: ")
                                encontradoAnimal = False
                                for animal in rebanho:
                                    if animal[1] == idBusca:
                                        print(f"Tipo: {animal[0]} | ID: {animal[1]} | Status: {animal[2]}")
                                        encontradoAnimal = True
                                        break
                                if not encontradoAnimal:
                                    print("Animal não encontrado.")

                        # PRODUÇÃO
                        elif opAdm == 2:
                            print("\n=== PRODUÇÃO ===")
                            print("1-Registrar leite")
                            print("2-Adicionar produto (Derivados)")
                            print("3-Listar estoque")

                            op = int(input("Escolha: "))

                            if op == 1:
                                litros = float(input("Litros produtos: "))
                                precoLeite = float(input("Preço de venda por litro: "))
                                
                                encontradoLeite = False
                                for p in estoqueProdutos:
                                    if p[0].lower() == "leite":
                                        p[1] += litros
                                        p[2] = precoLeite
                                        encontradoLeite = True
                                        break
                                
                                if not encontradoLeite:
                                    estoqueProdutos.append(["leite", litros, precoLeite])
                                
                                print("Leite registrado no estoque!")

                            elif op == 2:
                                nome = input("Produto (ex: Queijo Coalho): ")
                                qtd = float(input("Quantidade (kg): "))
                                valor = float(input("Preço por kg: "))

                                estoqueProdutos.append([nome, qtd, valor])
                                print("Produto adicionado ao estoque!")

                            elif op == 3:
                                if len(estoqueProdutos) == 0:
                                    print("Estoque vazio.")
                                for p in estoqueProdutos:
                                    if p[0].lower() == "leite":
                                        print(f"Item: {p[0]} | Qtd: {p[1]} Litros | Preço/L: R${p[2]}")
                                    else:
                                        print(f"Item: {p[0]} | Qtd: {p[1]} kg | Preço/kg: R${p[2]}")

                        # RELATÓRIO DETALHADO (R4 - TEMA LIVRE ADM)
                        elif opAdm == 3:
                            print("\n=== RELATÓRIO DE GESTÃO DA FAZENDA ===")
                            print(f"Total de animais no rebanho: {len(rebanho)}")
                            
                            leiteTotal = 0.0
                            queijoTotal = 0.0
                            for p in estoqueProdutos:
                                if p[0].lower() == "leite":
                                    leiteTotal += p[1]
                                else:
                                    queijoTotal += p[1]
                                    
                            print(f"Total de leite em estoque: {leiteTotal} Litros")
                            print(f"Total de derivados em estoque: {queijoTotal} kg")

                        elif opAdm == 4:
                            logado = False
                
                # ================= CLIENTE =================
                else:
                    while logado:
                        print("\n=== MENU CLIENTE ===")
                        print("1-Ver estoque de produtos")
                        print("2-Ver animais disponíveis")
                        print("3-Comprar")
                        print("4-Agendar retirada")
                        print("5-Meus agendamentos")
                        print("6-Meu Extrato de Gastos (Tema Livre)")
                        print("7-Logout")

                        op = int(input("Escolha: "))

                        if op == 1:
                            print("\n--- PRODUTOS EM ESTOQUE ---")
                            if len(estoqueProdutos) == 0:
                                print("Sem produtos no momento.")
                            for p in estoqueProdutos:
                                if p[0].lower() == "leite":
                                    print(f"Item: {p[0]} | Disponível: {p[1]} Litros | Preço/L: R${p[2]}")
                                else:
                                    print(f"Item: {p[0]} | Disponível: {p[1]} kg | Preço/kg: R${p[2]}")

                        elif op == 2:
                            print("\n--- ANIMAIS DISPONÍVEIS PARA VENDA ---")
                            temAnimaisvenda = False
                            for animal in rebanho:
                                if animal[2].lower() == "disponível para venda":
                                    print(f"Tipo: {animal[0]} | Identificação/ID: {animal[1]}")
                                    temAnimaisvenda = True
                            if not temAnimaisvenda:
                                print("Nenhum animal disponível para venda no momento.")

                        elif op == 3:
                            print("\nO que deseja comprar?")
                            print("1-Leite ou Derivados")
                            print("2-Animais")
                            tipoCompra = int(input("Escolha: "))

                            # COMPRA DE PRODUTOS (LEITE/QUEIJO)
                            if tipoCompra == 1:
                                nome = input("Digite o nome exato do produto: ")
                                qtdCompra = float(input("Quantidade que deseja comprar: "))

                                encontradoProduto = False
                                for p in estoqueProdutos:
                                    if p[0].lower() == nome.lower():
                                        encontradoProduto = True
                                        if p[1] >= qtdCompra:
                                            p[1] -= qtdCompra
                                            custo = qtdCompra * p[2]
                                            print(f"Compra realizada com sucesso! Valor: R${custo}")
                                            historicoCompras.append([user[1], nome, qtdCompra, custo])
                                        else:
                                            print(f"Quantidade insuficiente em estoque! Disponível: {p[1]}")
                                        break
                                
                                if not encontradoProduto:
                                    print("Produto não encontrado no estoque.")

                            # COMPRA DE ANIMAIS
                            elif tipoCompra == 2:
                                idAnimalCompra = input("Digite o ID do animal que deseja adquirir: ")
                                encontradoAnimal = False
                                
                                for animal in rebanho:
                                    if animal[1] == idAnimalCompra and animal[2].lower() == "disponível para venda":
                                        encontradoAnimal = True
                                        precoAnimal = float(input("Confirme o valor combinado do animal: R$"))
                                        
                                        rebanho.remove(animal) 
                                        
                                        print(f"Animal {animal[0]} (ID: {animal[1]}) adquirido com sucesso!")
                                        historicoCompras.append([user[1], f"Animal: {animal[0]} (ID: {animal[1]})", 1, precoAnimal])
                                        break
                                
                                if not encontradoAnimal:
                                    print("Animal não encontrado ou não está disponível para venda.")

                        elif op == 4:
                            data = input("Data (DD/MM/AAAA): ")
                            hora = input("Hora (HH:MM): ")
                            agendamentos.append([user[1], data, hora])
                            print("Retirada agendada com sucesso!")

                        elif op == 5:
                            print("\n--- SEUS AGENDAMENTOS ---")
                            temAgendamento = False
                            for ag in agendamentos:
                                if ag[0] == user[1]:
                                    print(f"Data: {ag[1]} às {ag[2]}")
                                    temAgendamento = True
                            if not temAgendamento:
                                print("Você não possui agendamentos.")

                        # EXTRATO DE GASTOS (R7 - TEMA LIVRE CLIENTE)
                        elif op == 6:
                            print(f"\n=== EXTRATO DE COMPRAS - {user[0]} ===")
                            totalGasto = 0.0
                            for compra in historicoCompras:
                                if compra[0] == user[1]:
                                    print(f"Item: {compra[1]} | Qtd: {compra[2]} | Total: R${compra[3]}")
                                    totalGasto += compra[3]
                            print(f"Valor total investido na fazenda: R${totalGasto}")

                        elif op == 7:
                            logado = False
                break

        if not encontrado:
            print("Login ou senha incorretos!")

    # CADASTRO
    elif cont == 2:
        print("\n=== CADASTRO ===")
        nome = input("Nome: ")
        email = input("Email (Seu login): ")

        senha = ""
        conf = "1"

        while senha != conf:
            senha = input("Senha: ")
            conf = input("Confirmar senha: ")
            if senha != conf:
                print("Senhas diferentes!")

        tipo = 0
        while tipo != 1 and tipo != 2:
            tipo = int(input("Tipo de conta (1-ADM | 2-CLIENTE): "))

        if tipo == 1:
            tipo = "administrador"
        else:
            tipo = "cliente"

        users.append([nome, email, senha, tipo])
        print("Cadastro realizado com sucesso!")

print("Sistema encerrado!")