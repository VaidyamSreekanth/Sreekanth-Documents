*** Settings ***
Documentation    To know how to do mathematical operations


*** Test Cases ***
Addition
    ${RV}    Evaluate    5 + 6
    log to console    \n addition of 5 + 6 = ${RV}

Sub
    ${r} =    Evaluate    45 - 5
    Log     test Case SUB ==> ${r}    ERROR



