
## Automação Cadastro de Cliente Zé com Robot Framework

Esse projeto tem como objetivo automizar os testes da opção de cadastro de novos usuários na aplicação Web da Zé 
delivery.  Abaixo estão listadas as tecnologias utilizadas na aplicação dos testes.
## Arquitetura do projeto
```
.
├── ze-code-challenge                           # Arquivos e pastas do framework.                       
    ├── results                                 # Pasta com logs e screenshots.
    ├── resources                    
      ├── keywords                              # Pasta que contém as keywords de config e page objects.
        ├── config.robot                        # Classe que contém as configurações do projeto: abrir/fechar app e desired capabilities.
        ├── kw_tela_cadastro.robot              # Classe que contém as ações e elementos da tela de cadastro.
        ├── kw_tela_login.robot                 # Classe que contém as ações e elementos da tela de login.
      ├── steps                                 # Pasta que contém steps do projeto.
        ├── cadastro_usuario_resources.robot    # Classe que contem os resources do projeto.
      ├── commons.robot                         # Arquivo que contém importações e bibliotecas do projeto.
    ├── tests                                   # Pasta que contém os testes do projeto.
      ├── cadastro_usuario_tests.robot          # Classe que contem os testes do projeto.
    ├── README.md                               # Documento do projeto.
    └── requirements.txt                        # Dependências do projeto.
    └── Makefile                                # Arquivo para automatizar o processo de execução.
    
```
## Technology

Estas são as tecnologias utilizadas no projeto:
  * RobotFramework 5.0.1
  * Robotframework-faker
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

>    $ make testeCadastroUsuario



