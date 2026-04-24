from entity import Cep
cep = Cep

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
    try:
        opcao = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))
        print()
        if opcao == 1:
            requisicao = input('Digite o cep: ')
            ceps_anteriores.append(cep.Cep(requisicao).search_cep(requisicao))
            print(cep.Cep(requisicao).search_cep(requisicao),"\n")
            if not input('Deseja procurar usar outro serviço? S/N ').upper() == 'S':
                print("Obrigado por usar nosso serviço, até mais!")
                break
        elif opcao == 2:
            if len(ceps_anteriores) == 0:
                print("Nenhum CEP na lista \n")
                print()

            for a,item in enumerate(ceps_anteriores,1):
                print(f'{a}°\n{item} \n')
        elif opcao == 3:
            print("Obrigado por usar nosso serviço, até mais!")
            break
        else:
            print("Essa opção não existe!")
    except ValueError:
        print("Essa opção não existe!")




