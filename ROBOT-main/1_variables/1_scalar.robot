*** Settings ***
Documentation   To know how to do scalar operations

*** Variables ***
${NAME}     Sri

*** Test Cases ***
Scalar Operations
    ${NAME}     Catenate    ${name}    Kumar
    Log    ${NAME}    WARN

*** Keywords ***
    
    