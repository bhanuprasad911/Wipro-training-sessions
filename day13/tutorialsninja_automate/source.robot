*** Settings ***

Library    SeleniumLibrary
Library    DataDriver    ${CURDIR}/Datasheet.xlsx    Sheet1    dialect=Excel
Suite Setup       Open TutorialsNinja
Test Template     TutorialsNinja signup With Excel
Suite Teardown    Close All Browsers

*** Variables ***
${url}      https://tutorialsninja.com/demo/
${browser}  chrome

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

TutorialsNinja signup With Excel
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}    ${confirmpassword}
    Click Element    xpath=//span[text()='My Account']
    Click Link    Register
    Wait Until Element Is Visible    name=firstname    10s
    Input Text    name=firstname    ${firstname}
    Input Text    name=lastname     ${lastname}
    Input Text    name=email        ${email}
    Input Text    name=telephone    ${telephone}
    Input Text    name=password     ${password}
    Input Text    name=confirm      ${confirmpassword}
    Click Element    name=newsletter
    Click Element    name=agree
    Click Button     xpath=//input[@value='Continue']
    Wait Until Element Is Visible    xpath=//h1[text()='Your Account Has Been Created!']    10s
    Click Element    xpath=//span[text()='My Account']
    Click Link       Logout
    Wait Until Element Is Visible    xpath=//h1[text()='Account Logout']    10s
    Click Element    xpath=//span[text()='My Account']
    Click Link       Login
    Wait Until Element Is Visible    name=email    10s
    Input Text    name=email        ${email}
    Input Text    name=password     ${password}
    Click Button     xpath=//input[@value='Login']
    Wait Until Element Is Visible    xpath=//h2[text()='My Account']    10s
    Click Element    xpath=//span[text()='My Account']
    Click Link       Logout

*** Test Cases ***
Signup with user from Excel
    [Tags]    DDT