*** Settings ***
Resource    ../keywords/restaurant_keywords.robot
Resource    ../keywords/user_keywords.robot
Resource    ../keywords/order_keywords.robot
Suite Setup    Create API Session

*** Test Cases ***
Add Rating
    Create Restaurant
    Create User
    Create Order
    ${body}=    Create Dictionary
    ...    order_id=1
    ...    rating=5
    ...    comment=Excellent
    ${response}=    POST On Session    foodie    /api/v1/ratings    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
