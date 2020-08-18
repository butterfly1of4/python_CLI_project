# python_CLI_project
# Contact book

This project allows a user to manage a contacts book from the command line. They can create new contacts, see a list of current contacts, get a listing of all contacts, and search for contacts by first name, update contacts, and delete contacts.
## Requirements:
This program was built using python and SQL with Peewee throught the CLI. To run this you will need:
    -Python 
    -Postgres, or another equivalent program to run SQL
    -Peewee
    -Knowledge of Python and SQL


## Opening the book
To access the contents of this app, you will need to do several things. 
    <dl>
        <dt>1. Make sure the latest version of Python is installed. I used Python 3.8.</dt>
        <dt>2. Check if PostgreseSQL or a similar Object-Relational Database softare is installed. </dt>
        <dt>3. Run
    ``` 
    pipenv install peewee psychopg2-binary autopep8
    ```</dt>
        <dt>4. Change into; ```pipenv shell``` to run the virtual environment.</dt>
        <dt>5. In one terminal, type: ```psql``` to enter into into the SQL shell.</dt>
    </dl>
    <!-- 6. Make sure there is a database created for your contacts to be store in. If you need to create one:
        ```CREATE DATABASE  <name>```
       -->
## Using the book:
Open the app, and run: ```python3 seed.py``` to seed the database initially. Also make sure to run ```\c contacts``` then ```SELECT * FROM Contacts;``` to seed the SQL tables.
Start the program: ```python3 main.py```
When the program is initiated, there will be a prompt that appears on the screen giving the user option of what they want to do with the app. The choices are: 

- Type 'all' to see a list of all the contacts
- Type 'new' to create a new contact
- To find a specific contact by first name, type the name of the person. 
    ***Note that the contacts are currently case-sensitive, so make sure the contact you entered is correct***
- Type 'update' to change a field in the contact.
- Type 'delete' to delete the entire contact.
- Type 'exit' to end the app.

All of these actions can be repeated until the program is exited.