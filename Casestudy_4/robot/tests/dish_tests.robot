*** Settings ***
Resource    ../keywords/dish_keywords.robot
Suite Setup    Create API Session

*** Test Cases ***
Add Dish
    Create Dish
Update Dish
    Create Restaurant
    Create Dish
    ${update}=    Create Dictionary    price=300
    ${response}=    PUT On Session    foodie    /api/v1/dishes/1    json=${update}
    Should Be Equal As Integers    ${response.status_code}    200

Delete Dish
    Create Restaurant
    Create Dish
    ${response}=    DELETE On Session    foodie    /api/v1/dishes/1
    Should Be Equal As Integers    ${response.status_code}    200
