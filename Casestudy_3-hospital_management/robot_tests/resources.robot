*** Settings ***
Documentation     Reusable keywords and variables for Hospital Management System.
Library           SeleniumLibrary

*** Variables ***
# Configuration
${URL}                http://127.0.0.1:5000
${BROWSER}            Chrome
${DELAY}              0.5s

# Locators (Form Fields)
${NAME_FIELD}         id=name
${AGE_FIELD}          id=age
${DISEASE_FIELD}      id=disease
${CONTACT_FIELD}      id=contact
${DOCTOR_DROPDOWN}    id=doctor
${SUBMIT_BUTTON}      id=submit_btn
${MESSAGE_AREA}       id=msg

*** Keywords ***
Open Hospital Portal
    [Documentation]    Opens the browser and navigates to the registration page.
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Register New Patient
    [Arguments]    ${name}    ${age}    ${disease}    ${contact}    ${doctor}
    [Documentation]    Fills out the registration form and clicks submit.
    Input Text      ${NAME_FIELD}       ${name}
    Input Text      ${AGE_FIELD}        ${age}
    Input Text      ${DISEASE_FIELD}    ${disease}
    Input Text      ${CONTACT_FIELD}    ${contact}
    Select From List By Value    ${DOCTOR_DROPDOWN}    ${doctor}
    Click Button    ${SUBMIT_BUTTON}

Verify Success Message
    [Arguments]    ${expected_msg}
    Wait Until Element Contains    ${MESSAGE_AREA}    ${expected_msg}
    Element Should Be Visible      ${MESSAGE_AREA}

Close Portal
    Close Browser