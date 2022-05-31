*** Keywords ***
Dado que estou na tela de login do Zé delivery
    Ir para pagina do Ze

Quando acessar a opção para cadastro de cliente
    Quero cadastrar uma conta no Ze

E preencho o formulario de cadastro
    [Arguments]  ${nomeCliente}  ${email}  ${pass}  ${cpf}  ${phone}  ${age}
    Preencher formulario de cadastro de cliente  ${nomeCliente}  ${email}  ${pass}  ${cpf}  ${phone}  ${age}

E preencho o formulário de cadastro de forma inválida
    [Arguments]  ${name}  ${email}  ${pass}  ${cpf}  ${tel}  ${dataNiver}
    Preencher formulario de cadastro de cliente  ${name}  ${email}  ${pass}  ${cpf}  ${tel}  ${dataNiver}

Entao é apresentado mensagem de alerta
    [Arguments]  ${campoObrigatorio}  ${msg}
    IF  '${campoObrigatorio}'=='name'
        Validar mensagem de alerta do campo nome      ${msg}
    ELSE IF  '${campoObrigatorio}'=='email'
        Validar mensagem de alerta do campo email     ${msg}
    ELSE IF  '${campoObrigatorio}'=='password'
        Validar mensagem de alerta do campo password  ${msg}
    ELSE IF  '${campoObrigatorio}'=='cpf'
        Validar mensagem de alerta do campo cpf       ${msg}
    ELSE IF  '${campoObrigatorio}'=='telefone'
        Validar mensagem de alerta do campo telefone  ${msg}
    ELSE IF  '${campoObrigatorio}'=='data'
        Validar mensagem de alerta do campo data      ${msg}
    ELSE
        Validar mensagem de alerta do campo nome      ${msg}
    END

E confirmar o envio do formulário
    Confirmar cadastro de usuario

E acionar opção para validar o celular depois
    Pular validacao de celular

Então é apresentada a tela inicial do Zé Delivery
    [Arguments]  ${userWelcome}
    Validar boas vindas usuario  ${userWelcome}