import entity.Cep

cep = entity.Cep
apresentacao = """-----------------------------------------
Bem vindo ao check CEP!
-----------------------------------------
"""
menu = """SELECIONE O SERVICO:
1-BUSCAR CEP
2-VER HISTÓRICO
3-SAIR
"""
print(apresentacao)
ceps_anteriores = []
while(True):
    print(menu)
    opcao = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))
    print()
    if opcao == 1:
        requisicao = input('Digite o cep: ')
        ceps_anteriores.append(cep.Cep(requisicao).search_cep(requisicao))
        print(cep.Cep(requisicao).search_cep(requisicao))
        if not input('Deseja proucurar usar outro serviço? S/N ').upper() == 'S':
            print("Obrigado por usar nosso serviço, até mais!")
            break
        print()
    elif opcao == 2:
        cont = 1
        if len(ceps_anteriores) == 0:
            print("Nenhum CEP na lista")
            print()
            continue

        for item in ceps_anteriores:
            print(f'{cont}° {item}')
        print()
    elif opcao == 3:
        print("Obrigado por usar nosso serviço, até mais!")
        break
    else:
        print("Essa opção não existe!")
        continue



