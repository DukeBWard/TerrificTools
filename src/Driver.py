# python, trying to remember

# Login page before this???

from controller import user_controller
from models.user_model import user_model

def driver(conn, cursor):
    
    command = "a"
    
    while command != "Quit":
        command = input("What's your command?: ")
        
        if command == "login":
            user = input("Username: ")
            password = input("Password: ")
            account = user_controller.login(conn, cursor, user, password)
            if account == False: 
                print("Login failed.")
                return 
            
            command = input(account.username + ": ")
            



        # calling the appropriate command based on input
