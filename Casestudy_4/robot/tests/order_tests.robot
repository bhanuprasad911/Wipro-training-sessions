*** Settings ***
Resource    ../keywords/restaurant_keywords.robot
Resource    ../keywords/user_keywords.robot
Resource    ../keywords/order_keywords.robot
Suite Setup    Create API Session

*** Test Cases ***
Place Order
    Create Restaurant
    Create User
    Create Order
Get Orders By Restaurant
    Create Restaurant
    Create User
    Create Order
    ${response}=    GET On Session    foodie    /api/v1/restaurants/1/orders
    Should Be Equal As Integers    ${response.status_code}    200

Get Orders By User
    Create Restaurant
    Create User
    Create Order
    ${response}=    GET On Session    foodie    /api/v1/users/1/orders
    Should Be Equal As Integers    ${response.status_code}    200
