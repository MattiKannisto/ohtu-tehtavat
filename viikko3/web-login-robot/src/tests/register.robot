*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testinimi
    Set Password  testisalasana1
    Set Password Confirmation  testisalasana1
    Submit Registration    
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testisalasana1
    Set Password Confirmation  testisalasana1
    Submit Registration    
    Page Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  testinimi
    Set Password  tes
    Set Password Confirmation  tes
    Submit Registration
    Page Should Contain  Password has to be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  testinimi
    Set Password  testisalasana1
    Set Password Confirmation  testisalakana2
    Submit Registration
    Page Should Contain  Password does not match password confirmation!

Login After Successful Registration
    Go To Login Page
    Set Username  testinimi
    Set Password  testisalasana1
    Submit Credentials
    Page Should Contain  Ohtu Application main page

Login After Failed Registration
    Go To Login Page
    Set Username  te
    Set Password  testisalasana1
    Submit Credentials
    Page Should Contain  Invalid username or password


*** Keywords ***
Submit Registration
    Click Button  Register

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}