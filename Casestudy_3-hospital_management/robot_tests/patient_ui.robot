*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            http://127.0.0.1:5000
${BROWSER}        Chrome

*** Test Cases ***
Verify Patient Registration
    Open Browser    ${URL}    ${BROWSER}
    Input Text      id=name       Charlie
    Input Text      id=age        22
    Input Text      id=disease    Headache
    Input Text      id=contact    112233
    Select From List By Value    id=doctor    Dr. Strange
    Click Button    id=submit_btn
    Wait Until Element Contains    id=msg    Patient added successfully
    [Teardown]    Close Browser