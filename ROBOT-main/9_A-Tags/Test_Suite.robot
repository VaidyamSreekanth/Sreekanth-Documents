*** settings ***
Documentation   To know how to use tags

*** Test Cases **
Testcase:1
    [Tags]    win
    Log    WIN TestCase 1    ERROR

Testcase:2
    [Tags]    Linux
    Log    Linux TestCase 2    ERROR

Testcase:3
    [Tags]    win
    Log    WIN TestCase 3    ERROR

Testcase:4
    [Tags]    MAC
    Log    MAC TestCase 4    ERROR

Testcase:5
    [Tags]    Linux
    Log    Linux TestCase 5    ERROR
