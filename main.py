dev = True

if dev == True:
    item1 = {
        "nome" : "Hipocloreto",
        "valor" : "32.50",
        "peso" : "5"
    }

    item2 = {
        "nome" : "Isopropilico",
        "valor" : "36.50",
        "peso" : "1"
    }

    item3 = {
        "nome" : "Formol",
        "valor" : "46.80",
        "peso" : "5"
    }
    product_list = [item1, item2, item3]
else:
    product_list = []

while True: 
    print("----MENU DE COLETA DE DADOS----")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Excluir")
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
            print("-"*9)
            for product in product_list:
                print("================================")
                print(f"Nome: {product ["nome"]}.")
                print(f"Valor: R${product["valor"]}.")
                print(f"Peso: {product["peso"]}KG.")
                print("================================")
        
        case 3: 
            name = input("Digite o nome de um produto para remover: ")
            for product in product_list:
                if product["nome"] == name:
                    product_list.remove(product)

        case 0:
            break
