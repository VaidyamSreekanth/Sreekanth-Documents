*** Settings ***
Documentation   *  To know how to use setup and teardown options *

*** Test Cases ***
Testcase1
    [Setup]       Log    Setup FOR FIRST TEST CASE    WARN
    Log    Test Case : 1   ERROR
    [Teardown]    Log    Teardown FOR FIRST TEST CASE    WARN

Testcase2
    [Setup]    Log    Setup FOR SECOND TEST CASE    WARN
    Log    Test Case : 2   ERROR
    [Teardown]    Teardown Section

*** Keywords ***
Teardown Section
    Log    TEARDOWN SECTION     WARN
    Log    ok

