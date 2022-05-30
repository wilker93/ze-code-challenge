*** Variables ***
${BROWSER}      chrome
${URl}          https://www.ze.delivery/conta/entrar

*** Keywords ***
Abrir o navegador
    Open Browser    browser=${BROWSER}
    Maximize Browser Window

Fechar o navegador
    Close Browser

Ir para pagina do Ze
    go to           url=${URl}

Realizar scroll da pagina
    Execute Javascript    window.scrollTo(100, document.body.scrollHeight)
    Execute Javascript    window.scrollTo(100, document.body.scrollHeight)
    Sleep   1

