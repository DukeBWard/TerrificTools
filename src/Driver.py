# python, trying to remember

# Login page before this???

from controller import user_controller
from models.user_model import user_model

def driver(conn, cursor):
    
    command = "a"
    
    while command.lower() != "quit":
        command = input("What's your command?: ")
        
        if command == "login":
            user = input("Username: ")
            password = input("Password: ")
            account = user_controller.login(conn, cursor, user, password)
            if not account: 
                print("Login failed.")
                signupIn = input("Would you like to sign up? (y/n)")
                if signupIn.lower() == 'y':
                    user = input("Username: ")
                    password = input("Password: ")
                    email = input("Email: ")
                    account = signup(conn, cursor, user, password, email)
                    print("User: "+user+" signed up")
                else:
                    return
        elif command.lower() == "signup" or command.lower() == "sign up":
            user = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            account = signup(conn, cursor, user, password, email)
            # 
            # Continue from this point assuming logged in or signed up
            # 
            command = input(account.username + ": ")
            



        # calling the appropriate command based on input
