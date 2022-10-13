# Login Page
# Totally uncompleted but something we can build on it
# we need to link a database of users to check for users


# Gets the user input for username and password

def login_input():
    user_name = input("Username: ")
    password = input("Password: ")

    validity = login_check(user_name, password)

    if validity == False:
        print("This user doesn't exist! Register or Try again...")
        response = True
        while response:
            decision = input("Register (R) or Try Again (TA)?: ")
            if decision == "TA":
                response = False    
                login_input()
            
            elif decision == "R":
                response = False
                register()
    
    else:
        print("User exists, accessing the database...")


# Registers the user into the database

def register():



# Checks for username and password match
# :param user_name: String
# :param password: String
# :return: True if there is an existing user

def login_check(user_name, password):
