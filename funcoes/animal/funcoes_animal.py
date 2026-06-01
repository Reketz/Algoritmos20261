def cadastrarAnimal(rebanho):
    tipo = input("Tipo animal (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): ")
    idAnimal = input("Identificação (Brinco/Número): ")
    status = input("Status (em lactação, para engorda, disponível para venda): ")

    rebanho.append([tipo, idAnimal, status])
    print("Animal cadastrado!")
