*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${URL}          https://demo.automationtesting.in/Register.html
${BROWSER}      chrome


*** Test Cases ***
Form Interaction Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    xpath=//input[@placeholder='First Name']    Bhanu
    Input Text    xpath=//input[@placeholder='Last Name']    Prasad

    Select Radio Button    radiooptions    Male

    Select Checkbox    id=checkbox1
    ${is_selected}=    Run Keyword And Return Status    Checkbox Should Be Selected    id=checkbox1
    IF    '${is_selected}' == 'True'    Log To Console    Cricket hobby selected

    Select From List By Label    id=Skills    Python

    Sleep    3s
    Close Browser
