*** Settings ***
Documentation   To know how to do list operations

*** Variables ***
@{NAMES}    sriram    Nagesh    Balu

*** Test Cases ***
List Operations
    Log    ${NAMES}          ERROR
    Log    ${NAMES}[0:2]       ERROR


