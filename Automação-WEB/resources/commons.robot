*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary    locale=pt_BR
Library     XML

Resource    keywords/config.robot
Resource    keywords/kw_tela_cadastro.robot
Resource    keywords/kw_tela_login.robot
Resource    steps/cadastro_usuario_resources.robot