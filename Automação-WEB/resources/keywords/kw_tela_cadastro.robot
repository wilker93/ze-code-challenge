*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${INPUT_NAME}           id=signup-form-input-name
${INPUT_EMAIL}          id=signup-form-input-email
${INPUT_PASSWORD}       id=signup-form-input-password
${INPUT_DOCUMENT}       id=signup-form-input-document
${INPUT_PHONE}          id=signup-form-input-phone
${INPUT_AGE}            id=signup-form-input-age
${CHECKBOX_TERMS}       id=sign-up-form-input-terms
${BTN_SIGNUP}           id=signup-form-button-signup
${BTN_VALIDATE_CEL}     id=confirm-phone-link-validate-later
${MSG_NAME_ALERT}       id=signup-form-input-name-error-message
${MSG_EMAIL_ALERT}      id=signup-form-input-email-error-message
${MSG_PASS_ALERT}       id=signup-form-input-password-error-message
${MSG_DOC_ALERT}        id=signup-form-input-document-error-message
${MSG_PHONE_ALERT}      id=signup-form-input-phone-error-message
${MSG_DATA_ALERT}       id=signup-form-input-age-error-message
${TITLE}                //title[contains(.,'Zé Delivery: Entrega de bebidas geladas a preço baixo')]
${ZE_LOGO}         id=ze-delivery-logo


*** Keywords ***
Preencher formulario de cadastro de cliente
    [Arguments]  ${nome}  ${email}  ${pass}  ${document}  ${phone}  ${idade}
    Wait Until Element Is Not Visible      ${BTN_CRIAR_CONTA}
    Input Text       ${INPUT_NAME}         ${nome}
    Input Text       ${INPUT_EMAIL}        ${email}
    Input Text       ${INPUT_PASSWORD}     ${pass}
    Input Text       ${INPUT_DOCUMENT}     ${document}
    Input Text       ${INPUT_PHONE}        ${phone}
    Input Text       ${INPUT_AGE}          ${idade}
    Realizar scroll da pagina
    Select Checkbox  ${CHECKBOX_TERMS}

Confirmar cadastro de usuario
    Click Button    ${BTN_SIGNUP}

Pular validacao de celular
    Wait Until Element Is Visible     ${BTN_VALIDATE_CEL}       30
    Realizar scroll da pagina
    Click Element       ${BTN_VALIDATE_CEL}

Validar tela inicial
    Wait Until Page Contains Element        ${ZE_LOGO}     30
    Click Element    address-search-input-address

Validar mensagem de alerta do campo nome
    [Arguments]  ${msg_alert}
    Page Should Contain Element  ${MSG_NAME_ALERT}  ${msg_alert}

Validar mensagem de alerta do campo email
    [Arguments]  ${msg_alert}
    Page Should Contain Element  ${MSG_EMAIL_ALERT}  ${msg_alert}

Validar mensagem de alerta do campo password
    [Arguments]  ${msg_alert}
    Page Should Contain Element  ${MSG_PASS_ALERT}  ${msg_alert}

Validar mensagem de alerta do campo cpf
    [Arguments]  ${msg_alert}
    Page Should Contain Element  ${MSG_DOC_ALERT}  ${msg_alert}

Validar mensagem de alerta do campo telefone
    [Arguments]  ${msg_alert}
    Page Should Contain Element  ${MSG_PHONE_ALERT}  ${msg_alert}

Validar mensagem de alerta do campo data
    [Arguments]  ${msg_alert}
    Page Should Contain Element  ${MSG_DATA_ALERT}  ${msg_alert}

