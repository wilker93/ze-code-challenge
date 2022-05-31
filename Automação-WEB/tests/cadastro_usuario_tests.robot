*** Settings ***
Documentation   Suite de testes para cadastro de usuário.
Resource        ../resources/commons.robot
Test Setup      Abrir o navegador
Test Teardown   Fechar o navegador

*** Test Cases ***

Caso de Teste 01 - Cadastro de usuário
    [Documentation]     Caso de teste para validar o cadastro de um novo usuário.
    [Tags]              cadastro    positivo
    ${AGE}          set variable  12122000
    ${PASSWORD}     set variable  @Challenge123
    ${DIGITFAKE}    set variable  619
    ${FIRSTNAMEFAKE}       FakerLibrary.First Name
    ${LASTNAMEFAKE}        FakerLibrary.Last Name
    ${MAILFAKE}            FakerLibrary.Email
    ${CPFFAKE}             FakerLibrary.cpf
    ${PHONEFAKE}           FakerLibrary.Random Number   digits=8    fix_len=8
    ${phoneNumber}  Catenate  ${DIGITFAKE}${PHONEFAKE}
    ${nomeCliente}  Catenate  ${FIRSTNAMEFAKE} ${LASTNAMEFAKE}

    Dado que estou na tela de login do Zé delivery
    Quando acessar a opção para cadastro de cliente
    E preencho o formulario de cadastro  ${nomeCliente}  ${MAILFAKE}  ${PASSWORD}  ${CPFFAKE}  ${phoneNumber}  ${AGE}
    E confirmar o envio do formulário
    E acionar opção para validar o celular depois
    Então é apresentada a tela inicial do Zé Delivery  ${nomeCliente}

Caso de Teste 02 - Cadastro de usuário - Nome do cliente não informado
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o nome do cliente não for informado.
    [Tags]              cadastro    exceção     Nome
    [Template]  Validar campos obrigatorios
    ${EMPTY}  wilker@bol.com.br  @Challenge123  42334323063  61996438523  10051994  name  Nome não pode ficar vazio

Caso de Teste 03 - Cadastro de usuário - Nome do cliente incorreto
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o nome do cliente é informado incorretamente.
    [Tags]              cadastro    exceção     Nome
    [Template]  Validar campos obrigatorios
    W  wilker@bol.com.br  @Challenge123  42334323063  61996438523  10051994  name  Seu nome não parece correto

Caso de Teste 04 - Cadastro de usuário - Sobrenome do cliente não informado
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o sobrenome do cliente não for informado.
    [Tags]              cadastro    exceção     Nome
    [Template]  Validar campos obrigatorios
    Wilker  wilker@bol.com.br  @Challenge123  42334323063  61996438523  10051994  name  Parece que você esqueceu do sobrenome

Caso de Teste 05 - Cadastro de usuário - E-mail do cliente não informado
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o e-mail do cliente não for informado.
    [Tags]              cadastro    exceção     e-mail
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  ${EMPTY}  @Challenge123  42334323063  61996438523  10051994  email  O campo e-mail não pode ficar vazio

Caso de Teste 06 - Cadastro de usuário - E-mail do cliente inválido
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o e-mail informado é inválido.
    [Tags]              cadastro    exceção     e-mail
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.  @Challenge123  42334323063  61996438523  10051994  email  Eita, esse e-mail não parece correto

Caso de Teste 07 - Cadastro de usuário - Senha do cliente não informada
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o senha do cliente não for informado.
    [Tags]              cadastro    exceção     senha
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  ${EMPTY}  42334323063  61996438523  10051994  password  O campo senha não pode ficar vazio

Caso de Teste 08 - Cadastro de usuário - Senha sem os requisitos mínimos
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o senha informada não atender os requisitos mínimos.
    [Tags]              cadastro    exceção     senha
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  Challenge123  42334323063  61996438523  10051994  password  O campo senha não pode ficar vazio

Caso de Teste 09 - Cadastro de usuário - CPF do cliente não informado
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o CPF do cliente não for informado.
    [Tags]              cadastro    exceção     cpf
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  ${EMPTY}  61996438523  10051994  cpf  O campo CPF não pode ficar vazio

Caso de Teste 10 - Cadastro de usuário - CPF do cliente inválido
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o CPF informado for inválido.
    [Tags]              cadastro    exceção     cpf
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  11111111111  61996438523  10051994  cpf  Seu CPF não parece correto

Caso de Teste 11 - Cadastro de usuário - Telefone do cliente não informado
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o telefone do cliente não for informado.
    [Tags]              cadastro    exceção     telefone
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  42334323063  ${EMPTY}  10051994  telefone  O campo Telefone não pode ficar vazio

Caso de Teste 12 - Cadastro de usuário - Telefone do cliente inválido
    [Documentation]     Caso de teste para validar o comportamento do sistema quando o telefone informado for inválido.
    [Tags]              cadastro    exceção     telefone
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  42334323063  61  10051994  telefone  Seu telefone não parece correto

Caso de Teste 13 - Cadastro de usuário - Data de nascimento não informado
    [Documentation]     Caso de teste para validar o comportamento do sistema quando data de nascimento não for informado.
    [Tags]              cadastro    exceção     telefone
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  42334323063  61996438523  ${EMPTY}  data  Data de nascimento não pode ficar vazia

Caso de Teste 14 - Cadastro de usuário - Data de nascimento inválida
    [Documentation]     Caso de teste para validar o comportamento do sistema quando data de nascimento for inválida.
    [Tags]              cadastro    exceção     telefone
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  42334323063  61996438523  1005  data  Data de nascimento não parece correta

Caso de Teste 15 - Cadastro de usuário - Usuário menor de idade
    [Documentation]     Caso de teste para validar o comportamento do sistema quando data de nascimento for inválida.
    [Tags]              cadastro    exceção     telefone
    [Template]  Validar campos obrigatorios
    Wilker Oliveira  wilker@bol.com.br  @Challenge123  42334323063  61996438523  10052020  data  Sua idade deve ser maior que 18 anos

***Keywords***
Validar campos obrigatorios
    [Documentation]     Caso de teste para validar os campos obrigatórios.
    [Arguments]  ${name}  ${email}  ${pass}  ${cpf}  ${tel}  ${dataNiver}  ${field}  ${msg}
    Dado que estou na tela de login do Zé delivery
    Quando acessar a opção para cadastro de cliente
    E preencho o formulário de cadastro de forma inválida  ${name}  ${email}  ${pass}  ${cpf}  ${tel}  ${dataNiver}
    Entao é apresentado mensagem de alerta  ${field}  ${msg}