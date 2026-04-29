from entity.Cep import Cep
cep = Cep()

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
while(True):
    print(menu)
    try:
        opcao = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))
        print()
        if opcao == 1:
            requisicao = input('Digite o cep: ')
            print(cep.search_cep(requisicao),"\n")
            if not input('Deseja procurar usar outro serviço? S/N ').upper() == 'S':
                print("Obrigado por usar nosso serviço, até mais!")
                break
        elif opcao == 2:
            cep.mostrar_ceps_anteriores()
        elif opcao == 3:
            print("Obrigado por usar nosso serviço, até mais!")
            break
        else:
            print("Essa opção não existe!")
    except ValueError:
        print("Essa opção não existe!")




