*** Settings ***
Library    D:/01_HexaEmbed/22Feb2026/03_libraries/SerialLibrary.py    COM7    9600

*** Test Cases ***
Echo Test One
    [Documentation]  This test case Four
    [Tags]           four  login
    Write Data    Four
    ${response}=    Read Data
    Should Be Equal    ${response}    Four
    Close Serial

Echo Test Two
    [Documentation]  This test case Five
    [Tags]           Five  login
    Write Data    Five
    ${response}=    Read Data
    Should Be Equal    ${response}    five
    Close Serial

Echo Test Three
    [Documentation]  This test case Six
    [Tags]           Six  login
    Write Data    Six
    ${response}=    Read Data
    Should Be Equal    ${response}    Six
    Close Serial