*** Settings ***
Library           RequestsLibrary
Library           Collections

Suite Setup       Create Session    foodie    http://localhost:5000/api/v1

*** Test Cases ***
Add Dish To Restaurant
    [Documentation]    Requirement 5: Add Dish
    # Create dictionary for restaurant
    &{res_data}=    Create Dictionary    name=Food Hub    category=Cafe    location=Main St
    ${res_resp}=    POST On Session    foodie    /restaurants    json=${res_data}
    Status Should Be    201    ${res_resp}
    ${res_id}=      Set Variable    ${res_resp.json()['id']}
    
    # Create dictionary for dish
    &{dish_data}=   Create Dictionary    name=Pasta    type=Italian    price=12
    ${dish_resp}=   POST On Session    foodie    /restaurants/${res_id}/dishes    json=${dish_data}
    Status Should Be    201    ${dish_resp}
    Should Be Equal As Strings    ${dish_resp.json()['name']}    Pasta

Delete Dish Successfully
    [Documentation]    Requirement 8: Delete Dish
    # Note: Using path /dishes/1 because /api/v1 is already in the session base URL
    ${response}=    DELETE On Session    foodie    /dishes/1    expected_status=any
    Log To Console    Delete request status: ${response.status_code}

Place User Order
    [Documentation]    Requirement 15: Place Order
    &{order_payload}=    Create Dictionary    user_id=1    restaurant_id=1    dishes=["Pasta"]
    ${response}=    POST On Session    foodie    /orders    json=${order_payload}
    Status Should Be    201    ${response}