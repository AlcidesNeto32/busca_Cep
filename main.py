import entity.Cep

cep = entity.Cep
apresentacao = """
    -----------------------------------------
             Bem vindo ao check CEP!
    -----------------------------------------
"""
print(apresentacao)
print()
while(True):
    requisicao = input('Digite o cep: ')
    print(cep.Cep(requisicao).search_cep(requisicao))
    if not input('Deseja proucurar outro cep? S/N ') == 'S':
        print("Obrigado por usar nosso serviço, até mais!")
        break
    print()



