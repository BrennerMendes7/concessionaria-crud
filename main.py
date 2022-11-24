opcao = 0
cliente = 0
moto = 0
venda = 0
lista_cliente = ["Brenner", "Alexandre", "Raquel"]
lista_moto = ["PCX 150", "Lead 110", "XTZ 250"]
lista_venda = []
while opcao != 4:
    opcao = int(input("1 - Gerenciar cliente    2 - Gerenciar moto    3 - Venda    4 - Sair : "))
    if opcao == 1:
        while cliente != 6:
            cliente = int(input("1 - Cadastrar cliente    2 - Editar cliente    3 - Excluir cliente    4 - Visualizar clientes    5 - Relatório de clientes    6 - Sair : "))
            if cliente == 1:
                nome_cliente = input("Digite o nome do cliente que deseja cadastrar: ")
                lista_cliente.append(nome_cliente)
                print("Cliente cadastrado com sucesso !")
            if cliente == 2:
                for (i, item) in enumerate(lista_cliente, start=0):
                    print("[", i, "-", item, "]")
                num_cliente = int(input("Digite o número do registro que deseja alterar: "))
                update_cliente = input("Digite o novo nome do cliente: ")
                lista_cliente[num_cliente] = update_cliente
                print("Cliente alterado com sucesso !")
            if cliente == 3:
                for (j, item2) in enumerate(lista_cliente, start=0):
                    print("[", j, "-", item2, "]")
                delete_cliente = int(input("Digite o número do registro que deseja excluir: "))
                lista_cliente.pop(delete_cliente)
                print("Cliente excluído com sucesso !")
            if cliente == 4:
                print(*lista_cliente, sep = ", ")
            if cliente == 5:
                arquivo = open("clientes.txt", "w")
                for aux in lista_cliente:
                   arquivo.write("%s \n" % aux)
                arquivo.close()
                print("Relatório de clientes criado com sucesso !")

    if opcao == 2:
        while moto != 6:
            moto = int(input("1 - Cadastrar moto    2 - Editar moto    3 - Excluir moto    4 - Visualizar motos    5 - Relatório de motos    6 - Sair : "))
            if moto == 1:
                nome_moto = input("Digite o nome do modelo da moto que deseja cadastrar: ")
                lista_moto.append(nome_moto)
                print("Moto cadastrada com sucesso !")
            if moto == 2:
                for (z, item3) in enumerate(lista_moto, start=0):
                    print("[", z, "-", item3, "]")
                num_moto = int(input("Digite o número do registro que deseja alterar: "))
                update_moto = input("Digite o novo nome do modelo da moto: ")
                lista_moto[num_moto] = update_moto
                print("Moto alterada com sucesso !")
            if moto == 3:
                for (l, item4) in enumerate(lista_moto, start=0):
                    print("[", l, "-", item4, "]")
                delete_moto = int(input("Digite o número do registro que deseja excluir: "))
                lista_moto.pop(delete_moto)
                print("Moto excluída com sucesso !")
            if moto == 4:
                print(*lista_moto, sep=", ")
            if moto == 5:
                arquivo2 = open("motos.txt", "w")
                for aux2 in lista_moto:
                    arquivo2.writelines("%s \n" % aux2)
                arquivo2.close()
                print("Relatório de motos criado com sucesso !")

    if opcao == 3:
        while venda != 5:
            venda = int(input("1 - Realizar venda    2 - Visualizar vendas concluídas    3 - Visualizar venda específica    4 - Relatório de vendas    5 - Sair : "))
            if venda == 1:
                for (c, item5) in enumerate(lista_cliente, start=0):
                    print("[", c, "-", item5, "]")
                venda_cliente = int(input("Digite o número do cliente que irá efetuar a compra: "))
                for (a, item6) in enumerate(lista_moto, start=0):
                    print("[", a, "-", item6, "]")
                venda_moto = int(input("Digite o número da moto que será vendida: "))
                lista_venda.append(lista_cliente[venda_cliente] + "/" + lista_moto[venda_moto])
                print("Venda concluída com sucesso !")
            if venda == 2:
                print(*lista_venda, sep=", ")
            if venda == 3:
                for (v, item7) in enumerate(lista_venda, start=0):
                    print(v, "-", item7)
                ler_venda = int(input("Qual dessas vendas você deseja visualizar: "))
                print(lista_venda[ler_venda])
            if venda == 4:
                arquivo3 = open("vendas.txt", "w")
                for aux3 in lista_venda:
                    arquivo3.writelines("%s \n" % aux3)
                arquivo3.close()
                print("Relatório de vendas criado com sucesso !")



