*** Settings ***
Documentation    To know how to create keywords


*** Test Cases ***
testcase:1
    Addition

testcase:2
    Subtraction    9    5


testcase:3
    ${RV} =    Multiplication    5    10
    Log      Multip OF 5 * 10 = ${RV}    ERROR


*** Keywords ***
Addition
    [Documentation]   Keyword without arguments
    ${SUM}    Evaluate    5 + 5
    Log    SUM OF 5 + 5 = ${SUM}    ERROR

Subtraction
    [Arguments]    ${A}    ${B}
    [Documentation]   Keyword with arguments
    ${SUM}    Evaluate    ${A} - ${B}
    Log    Subtraction OF ${A} - ${B} = ${SUM}    WARN

Multiplication    [Arguments]    ${A}    ${B}
    ${R}    Evaluate    ${A} * ${B}
    #[Return]    ${R}
    Return From Keyword If    2 == 6   ${R}

