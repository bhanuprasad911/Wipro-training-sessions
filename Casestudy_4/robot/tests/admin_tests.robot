*** Settings ***
Resource    ../keywords/restaurant_keywords.robot
Suite Setup    Create API Session

*** Test Cases ***
Admin Approve Restaurant
    Create Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/approve
    Should Be Equal As Integers    ${response.status_code}    200

Admin Disable Restaurant
    Create Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/disable
    Should Be Equal As Integers    ${response.status_code}    200

Admin Get Orders
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Should Be Equal As Integers    ${response.status_code}    200

Admin Get Feedback
    ${response}=    GET On Session    foodie    /api/v1/admin/feedback
    Should Be Equal As Integers    ${response.status_code}    200
