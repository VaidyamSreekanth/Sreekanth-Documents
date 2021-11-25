*** Settings ***
Documentation   To know how to do Dictionary operations

*** Variables ***
&{DICT}   name=kumar    eid=345    dname=IT

*** Test Cases ***
Dict Operations
    Log    ${DICT}    WARN
    Log    ${DICT}[name]    WARN

