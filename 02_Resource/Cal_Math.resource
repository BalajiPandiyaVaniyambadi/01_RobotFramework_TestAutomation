*** Settings ***
Documentation   Test Cal_Math Functionality
Library    D:/01_HexaEmbed/02_Git_Dwonload_Test/03_libraries/Cal_Math.py

*** Keywords ***
Perform Addition
    [Documentation]    Test Addition of Two Numbers
    [Tags]    Positive Test Case A + B
    [Arguments]    ${Var1}    ${Var2}    ${Exp_Res}
    ${Res}=    Cals Add    ${Var1}    ${Var2}
    Should Be Equal    ${Res}    ${Exp_Res}