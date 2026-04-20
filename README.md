# 📮 Check CEP

Sistema de consulta de CEPs brasileiros via linha de comando, utilizando a API pública [ViaCEP](https://viacep.com.br/).

---

## 📁 Estrutura do Projeto

```
check-cep/
│
├── entity/
│   └── Cep.py        # Classe responsável pela consulta do CEP
│
└── main.py           # Ponto de entrada da aplicação
```

---

## ✅ Funcionalidades

- Consulta de CEP via API ViaCEP
- Validação do formato do CEP (somente números, 8 dígitos)
- Exibição formatada dos dados: logradouro, bairro, cidade, UF, região e complemento
- Loop interativo para múltiplas consultas sem reiniciar o programa
- Tratamento de erros HTTP e de conexão

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca `requests`

### Instalação das dependências

```bash
pip install requests
```

### Execução

```bash
python main.py
```

---

## 🖥️ Exemplo de uso

```
-----------------------------------------
         Bem vindo ao check CEP!
-----------------------------------------
SELECIONE O SERVICO:
1-BUSCAR CEP
2-VER HISTÓRICO
3-SAIR

SELECIONE UMA DAS OPÇÕES ACIMA: 1

Digite o cep: 01310100

    ------------------------
    CEP: 55620-000
    COMPLEMENTO: 
    CIDADE: Glória do Goitá
    BAIRRO: 
    LOGRADOURO: 
    UF: PE
    REGIÃO: Nordeste
    ------------------------

Deseja procurar outro cep? S/N N
Obrigado por usar nosso serviço, até mais!
```

---

## ⚙️ Como funciona
###

A classe Cep é responsável por:

- Receber o CEP como parâmetro no construtor (`__init__`)
- Validar se o CEP contém apenas caracteres alfanuméricos e possui exatamente 8 dígitos
- Realizar a requisição HTTP à API do ViaCEP: `https://viacep.com.br/ws/{cep}/json/`
- Tratar erros de requisição (`HTTPError`, `RequestException`)
- Retornar os dados formatados ou uma mensagem de erro amigável

### 

O main é responsável por:

- Exibir a tela de boas-vindas
- Exibir o menu
- Instanciar e chamar o método `search_cep` da classe `Cep`
- Manter o loop de consultas ativo até o usuário digitar `N` ou Digitar 3


## 🔗 API utilizada

[ViaCEP](https://viacep.com.br/) — API gratuita e pública para consulta de CEPs brasileiros.

---

