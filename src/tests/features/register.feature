Feature: Registration
As a user
I want to register
So that I can use the system to help manage my export business

Background: Registration page
Given I have navigated to the registration page

Scenario: Successful registration
When I register with charles.moga1@gmail.com and assignmenT18
Then I should see a confirmation message

Scenario Outline: Unsuccessful attempt to register
When I register with <email>,<password>,<confirm_password>
Then I should see error <message>
Examples: account details
|email|password|confirm_password|message|
|charles.moga@gmail.com|assignmenT18|assignmenT18|Email already registered|
|charles.moga@gmail.com|assignmenT18|AssignmenT18|You must type the same password each time.|
|charles.moga@gmail.com|assignmenT  |assignmenT|This password contains letters only.|
|charles.moga@gmail.com|password18  |password18|This password contains the word 'password'|
|charles.moga@gmail.com|1234567890  |1234567890|This password is entirely numeric.|
|charles.moga@gmail.com|assign      |assign|This password is too short. It must contain at least 10 characters.|


Scenario: Attempt to register with invalid email
When I register with charles.moga and assignmenT18
Then the form will not be submitted

Scenario: Attempt to register when emails do not match
When I register with a@gmail.com, b@gmail.com
Then I should see the error You must type the same email each time. displayed
