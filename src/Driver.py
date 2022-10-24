# python, trying to remember

# Login page before this???

from controller.user_controller import *
from models.user_model import user_model

def driver(conn, cursor):
    
    command = ""
    account = None
    
    while True :
        command = input("Login or Sign up: ")
        
        if command.lower() == "help":
            print("Use one of the following commands: TODO")
            continue
        
        elif command.lower() == "quit" or command.lower() == "exit":
            return

        elif command.lower() == "login":
            user = input("Username: ")
            password = input("Password: ")
            account = login(conn, cursor, user, password)
            if not account: 
                print("Login failed.")
                signupIn = input("Would you like to sign up? (y/n)")
                if signupIn.lower() == 'y':
                    user = input("Username: ")
                    password = input("Password: ")
                    email = input("Email: ")
                    account = signup(conn, cursor, user, password, email)
                    print("User: "+user+" signed up")
                    continue
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
        
        while True and account:
            command = input(account.username + ": ")
            
            if command.lower() == "help":
                print("Use one of the following commands: TODO")
                continue

            elif command.lower() == "quit" or command.lower() == "exit":
                return
            
        
            



        # calling the appropriate command based on input
