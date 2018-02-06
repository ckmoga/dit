Feature: Registration
As a user
I want to register
So that I can use the system to help manage my export business


Scenario: Successful registration
Given I have navigated to the registration page
When I register with charles.moga1@gmail.com and assignmenT18
Then I should see a confirmation message

Scenario Outline: Unsuccessful attempt to register
When I register with <email>,<password>,<confirm_password>
Then I should see <message>
Examples: account details
|email|password|confirm_password|message|
|charles.moga@gmail.com|assignmenT18|assignmenT18|Email already registered|
|charles.moga@gmail.com|assignmenT18|AssignmenT18|Password does not match|
|charles               |assignmenT18|assignmenT18|Invalid email           |
|charles.moga@gmail.com|assignmenT  |assignmenT|Invalid password|
|charles.moga@gmail.com|password18  |password18|Invalid password|
|charles.moga@gmail.com|1234567890  |1234567890|Invalid password|
|charles.moga@gmail.com|assign      |assign|Invalid password|
