*** Settings ***
Documentation    Loop operations using list

*** Variables ***
@{names}     sriram    kumar    balu    nagesh

*** Test Cases ***
For Loop with list
    FOR    ${name}    IN    @{names}
      log    ${name}    WARN
      Log    OK
    END




