# python, trying to remember

# Login page before this???

from controller import user_controller

def driver(conn, cursor):
    
    command = "a"
    
    while command != "Quit":
        command = input("What's your command?: ")
        
        if command == "login":
            user = input("Username: ")
            password = input("Password: ")
            user_controller.login(cursor, user, password)


        # calling the appropriate command based on input
