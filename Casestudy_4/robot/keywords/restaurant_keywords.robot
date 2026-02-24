*** Settings ***
Resource    ../resources/common.resource

*** Keywords ***
Create Restaurant
    ${random}=    Generate Random String    5
    ${images}=    Create List    img1.jpg
    ${body}=    Create Dictionary
    ...    name=Food Hub ${random}
    ...    category=Indian
    ...    location=Hyderabad
    ...    images=${images}
    ...    contact=9876543210
    ${response}=    POST On Session    ${SESSION}    /api/v1/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
