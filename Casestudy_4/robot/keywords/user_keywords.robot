*** Settings ***
Resource    ../resources/common.resource

*** Keywords ***
Create User
    ${random}=    Generate Random String    5
    ${email}=    Set Variable    john${random}@test.com
    ${body}=    Create Dictionary
    ...    name=John
    ...    email=${email}
    ...    password=1234
    ${response}=    POST On Session    ${SESSION}    /api/v1/user/register    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
