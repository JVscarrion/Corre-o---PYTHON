funcionarios = {}

while True:
    print("-------/Menu de Opções\------")
    print("C - Cadastrar                ")
    print("A - Alterar                  ")
    print("E - Excluir                  ")
    print("P - Pesquisar                ")
    print("S - Sair                     ")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "S":
        print("Sair do Programa")
        break
    elif opcao == "C":
        Nome = input("Digite o nome do Funcionário: ")
        Cargo = input("Digite o cargo do Funcionário: ")
        funcionarios[Nome] = Cargo
        print("Funcionário Cadastrado")
    elif opcao == "A":
        Nome = input("Digite o nome do Funcionário que queira alterar: ")
        if Nome in funcionarios:
            Cargo = input("Digite o novo cargo do Funcionário: ")
            funcionarios[Nome] = Cargo
            print("Funcionário Alterado")
        else:
            print("Funcionário não encontrado")
    elif opcao == "E":
        Nome = input("Digite o nome do Funcionário que queira excluir: ")
        if Nome in funcionarios:
            del funcionarios[Nome]
        else:
            print("Funcionário não encontrado")
    elif opcao == "P": 
        listafuncionario = len(funcionarios)
        print(f"tamanho :{listafuncionario}")
        ordemalfabetica = sorted(funcionarios)
        for i in ordemalfabetica:
            print(i)