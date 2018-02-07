## Introduction
The project demonstrates the applictaion of BDD, Behave automation framework with implementation in python.

## Prerequisites
This project has been created in a linux environment and has not been validated in Windows or Mac OS environments, though it should not matter.
It is also assumed that the user has Chrome web browser installed and the executable is included in the path. This can usually be verified by launching Chrome application from command line.

## Setup
Install the following packages:

1. pip install git+https://github.com/behave/behave
2. pip install page_objects
3. pip install selenium

## Architectural overview
Behave is one of the common BDD frameworks that supports Gherkin. I have used WebbDriver to interact with the browser.

The project structure differs from default Behave structure. Behave.ini file instructs Behave where to look for feature files.

The general principle of good automation approach is to use page object models. Python happens to have a module specially built for this and I have made use of it here. The page object models I created are located in *src/tests/pages*

*src/tests/utils* folder contains helper file and a properties file. *test.properties* file contains properties that can be used throughout the project, for example we can define all menu items, footer links, urls, etc here. We then read and use them in any step definitions. This handy because it keeps tests clean and easy to maintain.
There is config.py utility to read the properties file and return the needed value to the caller.

## Running
To run the test, from the main project folder, type:

*behave*

If you want to printout error or debug messages, type:

*behave --no-capture*

## To do
1. Implement setup and teardown that can be called after every scenario. This is normally implemented in environment.py but there are currently problems with this when the project structure is customised like here.
2. Improve the page object models so that actions like filling forms are not performed in the step definitions themselves. This will make the tests clean, easy to understand/maintain and maximises re-usability. 
3. Improve testing menu and footer items by reading the web elements into lists and then iterating through the list. I have attempted to achieve this but run into framework issues, which will require time to debug and resolve.
4. Improve validation of invalid email addresses; currently we just verify that we are on the same page and submission has not proceeded.

## Defects
Currently the user can register using the same email address many times without any restriction. This certainly
is unusual unless the application has a way of gracefully handling this without showing error message to the user.

