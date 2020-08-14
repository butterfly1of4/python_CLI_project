# python_CLI_project
# Contact book

This project allows a user to manage a contacts book from the command line. They can create new contacts, see a list of current contacts, get a listing of all contacts, and search for contacts by first name. Update and delete features to come. 

## Requirements:
This program was built using python and SQL with Peewee throught the CLI. To run this you will need:
    -Python 
    -Postgres, or another equivalent program to run SQL
    -Peewee
    -Knowledge of Python and SQL


## Opening the book
To access the contents of this app, you will need to do several things. 
    1. Make sure the latest version of Python is installed. I used Python 3.8
    2. Check if PostgreseSQL or a similar Object-Relational Database softare is installed. 
    3. Run
    ``` pipenv install peewee psychopg2-binary autopep8```
    4. Change into; ```pipenv shell``` to run the virtual environment.
    5. In one terminal, type: ```psql``` to enter into into the SQL shell.
    <!-- 6. Make sure there is a database created for your contacts to be store in. If you need to create one:
        ```CREATE DATABASE  <name>```
       -->
## Using the book:
When the program is initiated, there will be a prompt that appears on the screen giving the user option of what they want to do with the app. The choices are: 

- Type 'all' to see a list of all the contacts
- Type 'new' to create a new contact
- To find a specific contact by first name, type the name of the person. 
    ***Note that the contacts are currently case-sensitive, so make sure the contact you entered is correct***
- Type 'exit' to end the app.

All of these actions can be repeated until the program is exited.