# python, trying to remember

# Login page before this???

from controller.user_controller import *
from controller.tools_controller import *
from controller.category_controller import *
from controller.catalog_controller import *
from controller.request_ticket_controller import *
from models.user_model import user_model
import pprint

def driver(conn, cursor):
    
    command = ""
    account = None
    
    while True :
        command = input("Login or sign up: ")
        
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
            command = command.split()
            
            # HELP
            if command[0].lower() == "help":
                print("Use one of the following commands: TODO")
                continue
            
            # QUIT/EXIT
            elif command[0].lower() == "quit" or command[0].lower() == "exit":
                return
            
            # SIGNOUT
            elif command[0].lower() == "sign out" or command[0].lower() == "signout":
                account = None
                break

            # SEARCH AND SORT
            elif command[0].lower() == "search" or command[0].lower() == "find":
                print()
             
                if command[1].lower() == "barcode":
                    records = search(conn,cursor,command[2],"barcode")

                elif command[1].lower() == "name":
                    param = " ".join(command[2:])
                    if len(command) == 3:
                        if command[2] == "asc" or command[2] == "desc":
                            records = sort(conn, cursor, command[2].lower(), command[1].lower())
                    else:
                        records = search(conn,cursor,param,"name")
                        
                elif command[1].lower() == "category":
                    if len(command) == 3:
                        if command[2] == "asc" or command[2] == "desc":
                            records = sort(conn, cursor, command[2].lower(), command[1].lower())
                    else:
                        records = search(conn,cursor,command[2],"category")

                if len(records) == 0:
                    print("Could not find that item.  Try again.")

                for row in records:
                    print("Barcode: {}".format(row[0]))
                    print("Borrowed: {}".format(row[1]))
                    print("Description: {}".format(row[2]))
                    print("Tool Name: {}".format(row[3]))
                    print("UserId: {}".format(row[4]))
                    print("Category: {}".format(row[5]))
                    print()

            # CREATE TICKET
            elif command[0].lower() == "cticket":
                date_needed = input("Date needed: ")
                duration = input("Duration: ")
                barcode = input("Tool barcode: ")
                create_ticket(conn, cursor, account, date_needed, duration, barcode)
                continue
                
        # calling the appropriate command based on input
