*** Settings ***
Resource    ../resources/common.resource
Resource    restaurant_keywords.robot

*** Keywords ***
Create Dish
    Create Restaurant
    ${body}=    Create Dictionary
    ...    name=Biryani
    ...    type=Veg
    ...    price=250
    ...    available_time=Lunch
    ${response}=    POST On Session    ${SESSION}    /api/v1/restaurants/1/dishes    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
