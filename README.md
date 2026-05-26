# Contact-Book
Contact Book
A simple terminal-based contact book built in Python to practice dictionaries.
What it does

Add a new contact (name, phone, email, tags)
View all contacts
Search for a contact by name
Delete a contact
Quit the program

How to run
python main.py
How to use
When the program starts you will see a menu:
1. Add contact
2. View all contacts
3. Search contact
4. Delete contact
5. Quit
Type a number and press Enter.
How data is stored
Each contact is stored as a dict inside the main contact dict:
pythoncontact = {
    "Ali": {
        "Phone": "070-123456",
        "Email": "ali@email.com",
        "Tag": "friend"
    }
}
What I learned

How to store data in a dictionary
How to use a dict inside a dict (nested dict)
How to loop through a dict using .items()
Difference between looping with for x in dict (keys only) vs for k, v in dict.items() (keys and values)
How to add, access, and delete keys in a dict
Using input() to get data from the user
Using a while loop to keep the program running
