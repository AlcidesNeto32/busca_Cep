import requests as rq

class Cep:

    def __init__(self,cep):
        self.cep = cep

    def search_cep(self,cep):
        if not self.cep.isalnum():
            return "Ops! o cep deve conter apenas números!"
        elif len(self.cep) != 8:
            return 'Ops! O CEP deve conter apenas 8 dígitos!'

        try:
             response = rq.get(f'https://viacep.com.br/ws/{self.cep}/json/')

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

        formatacao_dados = f"""

    ------------------------
    CEP: {cep}
    UF:{uf}
    CIDADE:{cidade}
    BAIRRO:{bairro}
    LOGRADOURO:{logradouro}
    COMPLEMENTO:{complemento}
    REGIAO:{regiao} 
    ------------------------
    """
        return formatacao_dados