*** settings ***
Documentation   This file is used to make math operations

*** Variables ***
${NAME}     SRIRAM


*** Keywords ***
Addition    [Arguments]    ${A}    ${B}
    ${R}    Evaluate    ${A} + ${B}
    Log    SUM OF ${A} + ${B} = ${R}    WARN

