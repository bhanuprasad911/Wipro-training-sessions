*** Settings ***
Documentation     Demo Suite showing Suite Setup/Teardown, Test Setup/Teardown, Tags
Library           SeleniumLibrary

Suite Setup       Open Application
Suite Teardown    Close Application

Test Setup        Start Test Case
Test Teardown     End Test Case

*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    chrome

*** Test Cases ***
Valid Login Test
    [Tags]    smoke    login
    Perform Login    standard_user    secret_sauce
    Page Should Contain    Products

Invalid Login Test
    [Tags]    regression    login
    Perform Login    wrong_user    wrong_pass
    Page Should Contain    Epic sadface

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=user-name    10s

Close Application
    Close All Browsers

Start Test Case
    Log To Console    \n=== Starting Test Case ===

End Test Case
    Log To Console    === Test Case Finished ===\n

Perform Login
    [Arguments]    ${username}    ${password}
    Input Text    id=user-name    ${username}
    Input Text    id=password     ${password}
    Click Button    id=login-button
