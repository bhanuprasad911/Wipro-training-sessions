*** Settings ***
Resource    ../keywords/user_keywords.robot
Suite Setup    Create API Session

*** Test Cases ***
User Registration
    Create User
Duplicate User Registration
    ${random}=    Generate Random String    5
    ${email}=    Set Variable    john${random}@test.com

    ${body}=    Create Dictionary
    ...    name=John
    ...    email=${email}
    ...    password=1234

    ${response1}=    POST On Session    foodie    /api/v1/user/register    json=${body}
    Should Be Equal As Integers    ${response1.status_code}    201

    ${response2}=    POST On Session    foodie    /api/v1/user/register    json=${body}    expected_status=409
    Should Be Equal As Integers    ${response2.status_code}    409
