
## Automação Cadastro de Cliente Zé com Robot Framework

Esse projeto tem como objetivo automizar os testes da API Open Weather, para obter o clima. 
API: http://openweathermap.org/current
Abaixo estão listadas as tecnologias utilizadas na aplicação dos testes.

## Arquitetura do projeto
```
.
├── test_automation_ze                          # Arquivos e pastas do framework.                       
    ├── .pytest_cache                           # Pasta com logs e cache do plugin pytest.
    ├── .venv                                   # Pasta contem arquivos para montar ambiente virtual.
    ├──  assets                                  
      ├── style.css                             # CSS gerado automatícamente pelo report para dar estilo a página de report.
    ├── tests                                   # Pasta que contem os testes
        ├── assets                                  
            ├── style.css                       # CSS gerado automatícamente pelo report para dar estilo a página de report.
        ├── conftest.py                         # Configurações dos testes.
        ├── test_openweathermap.py              # Classe que contém os testes da API.
    ├── pytest_report.html                      # Página com o resultado dos testes.   
    ├── README.md                               # Documento do projeto.
    └── requirements.txt                        # Dependências do projeto.
    
```
## Technology

Estas são as tecnologias utilizadas no projeto:
  * Pytest
  * Python 3.8.10
  * PyCharm


## Getting Started

### Foi utilizado ambiente windows para instalação do python, segue o passo a passo:

* Baixe o python na url https://www.python.org/downloads/release/python-392/ para a versão do windows 64.
* Realize a instalação expressa.
* Incluir a variável de ambiente do python no path.

### Instalando dependências do projeto

>    $ pip3 install -r requirements.txt


### Executando o projeto

>    $ pytest --html=pytest_report.html

>    Quando os testes finalizarem acesse o arquivo ../test_automation_ze/pytest_report.html no seu navegador e tenha acesso ao resultado dos testes.

