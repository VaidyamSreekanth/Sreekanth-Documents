*** Settings ***
Documentation   To know how to do list operations

Library    Collections

*** Variables ***
${ONE}     5

*** Test Cases ***
List Operations
    ${L}    Create List
    Append To List    ${L}   one   2   3   4
    log    List values are :: ${L}    WARN

    #${R} =    Get From List    ${L}    2
    #log    Second index value :: ${R}    WARN

    #Remove From List  ${L}   0
    #log    After removing based on index :: ${L}    #ERROR

    Remove Values From List   ${L}   3   4
    log    After removing based on value ==> ${L}    WARN
