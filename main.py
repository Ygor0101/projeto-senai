product_list = []

while True: 
    print("----MENU DE COLETA DE DADOS----")
    print("1. Cadastrar")
    print("2. Listar")
    print("0. Sair")
    print("-------------------------------")

    option = input("Escolha uma opção: ")

    match int(option):

        case 1:

            name_input = input("Digite o nome do produto: ")
            value_input = input("Digite o valor do seu produto: ")
            weight_input = input("Digite o peso do produto: ")

            new_product = {
                "nome": name_input,
                "valor": value_input,
                "peso": weight_input
            }

            product_list.append(new_product)
            print("Item cadastrado com sucesso!")

        case 2: 
            print(product_list)
            
        case 0:
            break
