*** Settings ***
Documentation    Loop operations using range function

*** Variables ***
${ONE}     10

*** Test Cases ***
Test For Loop
    FOR    ${INDEX}    IN RANGE    2    9    2
      log    ${INDEX}    WARN
    END

