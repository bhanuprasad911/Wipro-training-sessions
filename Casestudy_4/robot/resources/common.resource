*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String
Resource  ../variables/variables.robot


*** Keywords ***
Create API Session
    Create Session    ${SESSION}    ${BASE_URL}
