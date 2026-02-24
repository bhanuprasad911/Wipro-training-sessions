*** Settings ***
Resource    ../resources/common.resource

*** Keywords ***
Create Order
    ${dish_list}=    Create List    1
    ${body}=    Create Dictionary
    ...    user_id=1
    ...    restaurant_id=1
    ...    dishes=${dish_list}
    ${response}=    POST On Session    ${SESSION}    /api/v1/orders    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
