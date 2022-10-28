# python, trying to remember

# Login page before this???

from controller.user_controller import *
from controller.tools_controller import *
from controller.category_controller import *
from controller.catalog_controller import *
from controller.request_ticket_controller import *
from models.user_model import user_model
import pprint
from datetime import date


def driver(conn, cursor):
    command = ""
    account = None
    records = None
    order = None
    username = None

    while True:
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
                    print("User: " + user + " signed up")
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
                print("Use one of the following commands: \n\
                    quit: exit the app.\n\
                    sign out: sign out of current account\n\
                    search tools: search <name/barcode/category> <search param>\n\
                    sort tools: search <name/category> <asc/dsc>\n\
                    create ticket: cticket\n\
                    manage ticket: mticekt\n\
                    return tool: return\n")
                continue

            # QUIT/EXIT
            elif command[0].lower() == "quit" or command[0].lower() == "exit":
                return

            # SIGNOUT
            elif command[0].lower() == "sign" and command[1].lower() == "out" or command[0].lower() == "signout":
                account = None
                break

            # SEARCH AND SORT
            elif command[0].lower() == "search" or command[0].lower() == "find":
                print()

                if command[1].lower() == "barcode":
                    records = search(conn, cursor, command[2], "barcode")

                elif command[1].lower() == "name":
                    param = " ".join(command[2:])
                    if len(command) == 3:
                        if command[2] == "asc" or command[2] == "desc":
                            records = sort(conn, cursor, command[2].lower(), command[1].lower())
                        else:
                            records = search(conn, cursor, param, "name")
                    else:
                        records = search(conn, cursor, param, "name")

                elif command[1].lower() == "category":
                    if len(command) == 3:
                        if command[2] == "asc" or command[2] == "desc":
                            records = sort(conn, cursor, command[2].lower(), command[1].lower())
                        else:
                            records = search(conn, cursor, command[2], "category")
                    else:
                        records = search(conn, cursor, command[2], "category")

                if records == None:
                    print("Could not find that item.  Try again.")
                if records != None:
                    for row in records:
                        print("Barcode: {}".format(row[0]))
                        print("Available: {}".format(row[1]))
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

            # MANAGE TICKET
            elif command[0].lower() == "mticket":
                status = input("Incoming or Outgoing requests: ")
                if (status == "incoming"):
                    manage_incoming_tickets(conn, cursor, account)
                if (status == "outgoing"):
                    manage_outgoing_tickets(conn, cursor, account)

            # VIEW TOOLS
            elif command[0].lower() == "view":
                print()
                if command[1].lower() == "available":
                    print("Available Tools")
                    order = view(conn, cursor, command[1].lower())
                    if (order != None):
                        for row in order:
                            print("Tool name: {}".format(row[3]))
                    if (order == None):
                        print("No tools available!")
                elif command[1].lower() == "lent":
                    print("Tools Lent")
                    day = date.today()
                    order = view(conn, cursor, command[1].lower())
                    if (order != None):
                        for row in order:
                            username = getuser(conn, cursor, row[18])
                            print("Tool name: {}".format(row[3]))  # name
                            print("User borrowing tool: " + ''.join(username[0]))
                            print("Return by: {}".format(row[20]))  # return date
                            if row[20] < day:
                                print("This tool is overdue!")
                                print('\n')
                    if (order == None):
                        print("No tools lent!")
                elif command[1].lower() == "borrowed":
                    print("Tools Borrowed")
                    day = date.today()
                    order = view(conn, cursor, command[1].lower())
                    if (order != None):
                        for row in order:
                            username = getuser(conn, cursor, row[19])
                            print("Tool name: {}".format(row[3]))
                            print("Tool owner: " + ''.join(username[0]))
                            print("Return by: {}".format(row[20]))

                            if row[20] < day:
                                print("This tool is overdue!")
                                print('\n')
                    if (order == None):
                        print("No tools borrowed!")

                # RETURN TOOLS
            elif command[0].lower() == "return":
                return_borrowed_tool(conn, cursor, account)

            elif command[0].lower() == 'ccategory':
                create_category(conn, cursor)

            elif command[0].lower() == "printcatalog":
                print_catalog(conn, cursor, account)

            elif command[0].lower() == "editdescription":
                edit_description(conn, cursor)

            elif command[0].lower() == "edittoolname":
                edit_tool_name(conn, cursor)

            elif command[0].lower() == "addcategory":
                add_category(conn, cursor)

            elif command[0].lower() == "removecategory":
                remove_category(conn, cursor)

            elif command[0].lower() == "removetool":
                remove_tool(conn, cursor)

            elif command[0].lower() == "createtool":
                create_tool(conn, cursor, account)

