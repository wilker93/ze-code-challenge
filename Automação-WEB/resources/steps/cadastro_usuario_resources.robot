*** Variables ***
${AGE}          12122000
${PASSWORD}     @Challenge123
${DIGITFAKE}    619

*** Keywords ***
Dado que estou na tela de login do Zé delivery
    Ir para pagina do Ze

Quando acessar a opção para cadastro de cliente
    Quero cadastrar uma conta no Ze

E preencho o formulario de cadastro
    ${FIRSTNAMEFAKE}       FakerLibrary.First Name
    ${LASTNAMEFAKE}        FakerLibrary.Last Name
    ${MAILFAKE}            FakerLibrary.Email
    ${CPFFAKE}             FakerLibrary.cpf
    ${PHONEFAKE}           FakerLibrary.Random Number   digits=8    fix_len=8

    ${phoneNumber}  Catenate  ${DIGITFAKE}${PHONEFAKE}
    ${nomeCliente}  Catenate  ${FIRSTNAMEFAKE} ${LASTNAMEFAKE}
    Preencher formulario de cadastro de cliente  ${nomeCliente}  ${MAILFAKE}  ${PASSWORD}  ${CPFFAKE}  ${phoneNumber}  ${AGE}

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
    Validar tela inicial


E informar os dados de usuário menos o nome e sobrenome

    ${MAILFAKE}            FakerLibrary.Email
    ${CPFFAKE}             FakerLibrary.cpf
    ${PHONEFAKE}           FakerLibrary.Random Number   digits=8    fix_len=8

    Wait Until Element Is Not Visible       onetrust-reject-all-handler
    Click Element     signup-form-input-name
    Input Text      signup-form-input-email        ${MAILFAKE}
    Input Text      signup-form-input-password     ${PASSWORD}
    Input Text      signup-form-input-document     ${CPFFAKE}
    Input Text      signup-form-input-phone        ${DIGITFAKE}+${PHONEFAKE}
    Input Text      signup-form-input-age          ${AGE}
    Realizar scroll da pagina
    Select Checkbox     sign-up-form-input-terms

E informar os dados de usuário com um nome inválido
    ${FIRSTNAMEFAKE}       FakerLibrary.First Name
    ${LASTNAMEFAKE}        FakerLibrary.Last Name
    ${MAILFAKE}            FakerLibrary.Email
    ${CPFFAKE}             FakerLibrary.cpf
    ${PHONEFAKE}           FakerLibrary.Random Number   digits=8    fix_len=8

    Wait Until Element Is Not Visible       onetrust-reject-all-handler
    Input Text      signup-form-input-name         Sr. ${FIRSTNAMEFAKE} ${LASTNAMEFAKE}
    Input Text      signup-form-input-email        ${MAILFAKE}
    Input Text      signup-form-input-password     ${PASSWORD}
    Input Text      signup-form-input-document     ${CPFFAKE}
    Input Text      signup-form-input-phone        ${DIGITFAKE}+${PHONEFAKE}
    Input Text      signup-form-input-age          ${AGE}
    Realizar scroll da pagina
    Select Checkbox     sign-up-form-input-terms

E informar os dados de usuário menos sobrenome
    ${FIRSTNAMEFAKE}       FakerLibrary.First Name
    ${LASTNAMEFAKE}        FakerLibrary.Last Name
    ${MAILFAKE}            FakerLibrary.Email
    ${CPFFAKE}             FakerLibrary.cpf
    ${PHONEFAKE}           FakerLibrary.Random Number   digits=8    fix_len=8

    Wait Until Element Is Not Visible       onetrust-reject-all-handler
    Input Text      signup-form-input-name         ${FIRSTNAMEFAKE}
    Input Text      signup-form-input-email        ${MAILFAKE}
    Input Text      signup-form-input-password     ${PASSWORD}
    Input Text      signup-form-input-document     ${CPFFAKE}
    Input Text      signup-form-input-phone        ${DIGITFAKE}+${PHONEFAKE}
    Input Text      signup-form-input-age          ${AGE}
    Realizar scroll da pagina
    Select Checkbox     sign-up-form-input-terms



Então é apresentada a mensagem de erro "${EMPTYNAME}"
    Wait Until Element Is Visible   //p[@aria-live='assertive'][contains(.,'${EMPTYNAME}')]

E o botão para prosseguir fica desabilitado
    Element Should Be Disabled    signup-form-button-signup