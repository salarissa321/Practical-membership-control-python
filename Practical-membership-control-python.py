



#------------------------------------------------
#------- Practical Membership Control-----
#-------------------------------------------------


# List Contains Admins

admins = ["Salar" , "aboAbass" , "aboSaed" , "aboDlo" , "aboViyan" , "aboGmlo" , "Kasabeh"]
# print(admins.index("Abo Saed")) # 2

print(admins) # ['Salar', 'Abo Abass', 'Abo Saed', 'Abo Dlo', 'Abo Viyan', 'Abo Gmlo', 'Kasabeh']
# admins[1] = "Hamada" # # ['Salar', 'Hamada', 'Abo Saed', 'Abo Dlo', 'Abo Viyan', 'Abo Gmlo', 'Kasabeh']
admins[admins.index("Abo Abass")] = "Hamada" # ['Salar', 'Hamada', 'Abo Saed', 'Abo Dlo', 'Abo Viyan', 'Abo Gmlo', 'Kasabeh']
print(admins) ## ['Salar', 'Hamada', 'Abo Saed', 'Abo Dlo', 'Abo Viyan', 'Abo Gmlo', 'Kasabeh']

# Login

name = input(" Please Type Your Name ").strip().capitalize() #  Please Type Your Name Salar

# If Name is In Admin

if name in admins:

    print("You Are Admin") # Salar # You Are Admin
    print(f"Hello {name} Welcome Back") # Hello Salar Welcome Back

    option = input("Delete Or Update Your Name ?").strip().capitalize() # Delete Or Update Your Name ? delete or Update
    # Update Option
    print(option) # Delete Or Update
    if option == "Update" or option == "U" :
        theNewName = input("Your New Name Please").strip().capitalize() # Your New Name Please Issa
        print(theNewName) # Issa
        admins[admins.index(name)] = theNewName 
        print("Name Updated") # Name Updated
        print(admins) # ['Issa', 'Abo Abass', 'Abo Saed', 'Abo Dlo', 'Abo Viyan', 'Abo Gmlo', 'Kasabeh']

    # Delete Option
    elif option == "Delete" or option == "D" :
        print(option) # Delete
        admins.remove(name)
        print("Name Deleted") # Name Deleted
        print(admins) # ['Abo Abass', 'Abo Saed', 'Abo Dlo', 'Abo Viyan', 'Abo Gmlo', 'Kasabeh']
    # Wrong Option
    else :
        print("Wrong Option Choosed") # Wrong Option Choosed
        
        
    

    

else :

    print("You Are not Admin")
    status = input("Not Admin, Add you Y,N ?").strip().capitalize()

    if status == "Yes" or "Y" :
        print("You Have been Added")
        admins.append(name)
        print(admins) # # ['Salar', 'aboAbass', 'aboSaed', 'aboDlo', 'aboViyan', 'aboGmlo', 'Kasabeh', 'Salem']
    else :
        print("you Are not Added") 