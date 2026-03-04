*** Settings ***
Library    D:/01_HexaEmbed/22Feb2026/03_libraries/SerialLibrary.py    COM8    9600

*** Test Cases ***
Echo Test One
    [Documentation]  This test case One
    [Tags]           One  login
    Write Data    One
    ${response}=    Read Data
    Should Be Equal    ${response}    One
    Close Serial

Echo Test Two
    [Documentation]  This test case Two
    [Tags]           Two  login
    Write Data    Two
    ${response}=    Read Data
    Should Be Equal    ${response}    Two
    Close Serial

Echo Test Three
    [Documentation]  This test case Three
    [Tags]           Three  login
    Write Data    Three
    ${response}=    Read Data
    Should Be Equal    ${response}    Three
    Close Serial