*** Settings ***
Documentation   Test Cal_Math Libray Functionality
Resource    D:/01_HexaEmbed/02_Git_Dwonload_Test/02_Resource/Cal_Math.resource

*** Test Cases ***
Postive Addition
    [Documentation]  Postive Addition Test
    [Tags]           Postive Addition Test
    Perform Addition    5   6   11

One More Time
    [Documentation]  One More Time
    [Tags]           One More Time Test
    Perform Addition    3    4    7
