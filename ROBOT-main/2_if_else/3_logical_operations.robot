*** Settings ***
Documentation    To know how to use logical operations
Library    Collections

*** Variables ***
${ONE}    8

*** Test Cases ***
Logical Operations
    Run Keyword If   2 >= 4 or ${ONE} == 8   Log     LOGICAL OR \n    WARN

    Run Keyword If   2 > 1 and ${ONE} == 8   Log    LOGICAL AND \n    WARN
