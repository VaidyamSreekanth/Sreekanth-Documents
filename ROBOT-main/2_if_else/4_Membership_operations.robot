*** Settings ***
Documentation    To know how to use Membership operations

*** Variables ***
@{NAMES}    Sriram    balu    nagesh
${NAME}     'sriram'

*** Test Cases ***
Membership Operations
    Run Keyword If   'sri' in ${NAME}    Log   IN    ERROR

    #Run Keyword If   'Sri' not in ${NAMES}   Log   NOT #IN     ERROR

