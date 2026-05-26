
contact = {} 
user__input = ''


while user__input != '5': 
    print("--------------Contact Book-----------------------")
    print ("1.Add contact ")
    print ("2.View all contacts ")
    print ("3.Search contact ")
    print ("4.Delete contact ")
    print ("5.Quit ") 
    user__input = input("Pick a nummer: ")
    
    if user__input == "1":
        print (" # --- ADD CONTACT ---")
        Name = input   ("Name: ")
        Phone = input  ("Phone: ")
        Email = input ("Emails: ")
        Tag = input    ("Tag: ")

        contact[Name] ={
            "Phone": Phone,
            "Email": Email,
            "Tag" : Tag,}

    elif user__input == "2": 
        if len(contact) == 0:
            print ("the contact book is empty")

        else : 
          print ("-------------ALl the list------------------")
          for name,details in contact.items():
            print ("Name=",name )
            print ("Phone=", details ["Phone"])
            print ("Email=", details["Email"])
            print ("Tag =", details["Tag"])
            print ("==================")

    elif user__input == "3": 
        searched_name = input ("Enter The Name: ")
        
        for details in contact: 
           details = contact[searched_name]
           print('- - - - - - - - -- Result - - - - - - -  - - -')
           print (f"name= {searched_name}" )
           print ("Phone", details["Phone"])
           print ( "Email",details["Email"])
           print ("Tag =", details["Tag"]) 
        
    elif user__input == "4": 
       name = input ("Name :")
       
       if name in contact: 
        del (contact[Name])
        print("Deleted !!")
       else:
          print ("Contact not found")


    elif user__input == "5": 
       print ("GoodBye!")
       break
    else:
     print("Please pick a number between 1 and 5")
