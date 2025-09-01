# Bem-vindo ao sistema
print("Olá! Seja bem-vindo ao sistema de gestão de Natan Jose Maria.")

# Lista para armazenar funcionários (lista de dicionários)
lista_funcionarios = []

# ID inicial baseado no seu RU (coloquei o correto aqui)
id_global = 5168996

# Função para cadastrar funcionário
def cadastrar_funcionario(id):
    print(f"\n--- Cadastro de Funcionário (ID: {id}) ---")
    nome = input("Nome do funcionário: ")
    setor = input("Setor do funcionário: ")
    salario = input("Salário do funcionário: ")

    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_funcionarios.append(funcionario.copy())  # copia o dicionário para a lista
    print("Funcionário cadastrado com sucesso!")

# Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print("\n--- CONSULTAR FUNCIONÁRIO ---")
        print("1 - Consultar Todos")
        print("2 - Consultar por ID")
        print("3 - Consultar por Setor")
        print("4 - Voltar ao Menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- LISTA DE FUNCIONÁRIOS ---")
            for func in lista_funcionarios:
                print(func)

        elif opcao == "2":
            id_consulta = input("Digite o ID do funcionário: ")
            encontrado = False
            for func in lista_funcionarios:
                if str(func["id"]) == id_consulta:
                    print(func)
                    encontrado = True
            if not encontrado:
                print("Funcionário com esse ID não encontrado.")

        elif opcao == "3":
            setor_consulta = input("Digite o nome do setor: ")
            achou = False
            for func in lista_funcionarios:
                if func["setor"].lower() == setor_consulta.lower():
                    print(func)
                    achou = True
            if not achou:
                print("Nenhum funcionário encontrado nesse setor.")

        elif opcao == "4":
            return  # Volta ao menu principal

        else:
            print("Opção inválida. Tente novamente.")

# Função para remover funcionário
def remover_funcionario():
    while True:
        print("\n--- REMOVER FUNCIONÁRIO ---")
        id_remove = input("Digite o ID do funcionário a remover: ")
        for func in lista_funcionarios:
            if str(func["id"]) == id_remove:
                lista_funcionarios.remove(func)
                print("Funcionário removido com sucesso.")
                return
        print("ID inválido. Tente novamente.")

# -------------------------------
# MENU PRINCIPAL (main)
# -------------------------------
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Remover Funcionário")
    print("4 - Encerrar Programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_funcionario(id_global)
        id_global += 1  # incrementa ID para próximo funcionário

    elif opcao == "2":
        consultar_funcionarios()

    elif opcao == "3":
        remover_funcionario()

    elif opcao == "4":
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Opção inválida. Escolha entre 1 e 4.")
