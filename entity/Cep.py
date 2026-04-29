import requests as rq
import functools
import re

class Cep:

    def __init__(self):
        pass

    global historico_cep
    historico_cep = []

    @functools.cache
    def search_cep(self,cep):
        padrao_cep = re.compile(r'(\d){5}|-(\d){3}')

        if not padrao_cep.match(cep):
            return f"O CEP: {cep} está inválido!"
        
        try:
             response = rq.get(f'https://viacep.com.br/ws/{cep}/json/')
             response.raise_for_status()

        except rq.exceptions.HTTPError as e:
            return f"Erro HTTP: {e}"

        except rq.exceptions.RequestException as e:
            return f"Erro inesperado na requisição: {e}"

        dados = response.json()

        if 'erro' in dados:
            return 'Ops! esse CEP não existe!'

        cep = dados['cep']
        logradouro = dados['logradouro']
        complemento = dados['complemento']
        bairro = dados['bairro']
        cidade = dados['localidade']
        uf = dados['uf']
        regiao = dados['regiao']

        formatacao_dados =f"""CEP: {cep}
COMPLEMENTO: {complemento}
CIDADE: {cidade}
BAIRRO: {bairro}
LOGRADOURO: {logradouro}
UF: {uf}
REGIÃO: {regiao}"""
        historico_cep.append(formatacao_dados)
        return formatacao_dados
    

    def mostrar_ceps_anteriores(self):
        if len(historico_cep) == 0:
            return 'Nenhum cep no histórico!'

        for pos,item in enumerate(historico_cep,1):
            print (f'{pos}°\n{item}\n')


