*** Settings ***
Resource    ../keywords/restaurant_keywords.robot
Suite Setup    Create API Session

*** Test Cases ***
Add Restaurant
    Create Restaurant
Get Restaurant
    Create Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/1
    Should Be Equal As Integers    ${response.status_code}    200
Search Restaurant
    ${params}=    Create Dictionary    location=Hyderabad
    ${response}=    GET On Session    ${SESSION}    /api/v1/restaurants/search    params=${params}
    Should Be Equal As Integers    ${response.status_code}    200
