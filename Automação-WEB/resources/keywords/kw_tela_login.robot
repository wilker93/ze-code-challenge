*** Variables ***
${BTN_CRIAR_CONTA}      id=create-account-link  
${TITLE_CRIAR_CONTA}    Criar conta com e‑mail e senha

*** Keywords ***
Quero cadastrar uma conta no Ze
    Click Element                ${BTN_CRIAR_CONTA}
    Wait Until Page Contains     ${TITLE_CRIAR_CONTA}