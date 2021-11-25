*** Settings ***
Documentation   To know how to do Dict operations

Library    Collections

*** Variables ***
${TWO}    sriram

*** Test Cases ***
Dict Operations
    ${D}    Create Dictionary    name=${TWO}    dno=34
    Log     Dict is :: ${D}    WARN

    #${r}    Get From Dictionary    ${D}    name
    #Log     Name is : ${r}     WARN

    #${K}    Get Dictionary Keys    ${D}
    #Log     Keys are : ${K}     WARN

    Remove From Dictionary    ${D}    name
    Log     Dict IS :: ${D}    WARN

