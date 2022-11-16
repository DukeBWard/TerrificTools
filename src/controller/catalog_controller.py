from . import category_controller


def print_catalog(conn, cursor, user):
    userid = user.userid
    cursor.execute(f"select * from tools_table where userid={userid}")
    catalog = cursor.fetchall()
    if catalog is None:
        print("You do not have any tools in your catalog")
    for row in catalog:
        print("Barcode: {}".format(row[0]))
        print("Borrowed: {}".format(row[1]))
        print("Description: {}".format(row[2]))
        print("Tool Name: {}".format(row[3]))
        print("UserId: {}".format(row[4]))
        print("Category: {}".format(row[5]))
        print()


def remove_tool(conn, cursor):
    tool_barcode = input("Which tool would you like (please type barcode): ")
    cursor.execute(f"select * from request_ticket_table where barcode={tool_barcode}")
    check = cursor.fetchall()
    if len(check) == 0:
        cursor.execute(f"delete from tools_table where barcode ={tool_barcode}")
        conn.commit()
    else:
        print("Is currently being borrowed and cannot be deleted")


def edit_description(conn, cursor):
    tool_barcode = input("Which tool would you like (please type barcode): ")
    description_new = input("Enter new description for this tool: ")
    cursor.execute(f"update tools_table set description='{description_new}' where barcode={tool_barcode}")
    conn.commit()


def edit_tool_name(conn, cursor):
    tool_barcode = input("Which tool would you like (please type barcode): ")
    tool_name = input("Enter new name for this tool: ")
    cursor.execute(f"update tools_table set tool_name='{tool_name}' where barcode='{tool_barcode}'")
    conn.commit()


def add_category(conn, cursor):
    tool_barcode = input("Which tool would you like (please type barcode): ")
    category = category_controller.search_category(conn, cursor)
    cursor.execute(f"select * from tools_table where barcode={tool_barcode}")
    category_array = cursor.fetchone()
    category_array[5].append(category)
    conn.commit()


def remove_category(conn, cursor):
    tool_barcode = input("Which tool would you like (please type barcode): ")
    category = category_controller.search_category(conn, cursor)
    cursor.execute(f"select * from tools_table where barcode={tool_barcode}")
    categoryArray = cursor.fetchone()
    categoryArray[5].remove(category)


def view_dashboard(conn, cursor, user):
    
    userid = user.userid
    
    cursor.execute(f"select count(*) from tools_table where userid={userid}")
    count = cursor.fetchall()
    print("Number of tools available from your catalog: " + str(count[0][0]))
    
    # Lent tool means it is currently being used by someone else and not returned (not a previous lent)
    cursor.execute(f"select count(*) from request_ticket_table where toolowner={userid} and status = 'accepted'")
    lent = cursor.fetchall()
    print("Number of tools you lent: " + str(lent[0][0]))
    
    # borrowed means, it is currently in possesion of the user (not previously borrowed and returned)
    cursor.execute(f"select count(*) from request_ticket_table where userid={userid} and status = 'accepted'")
    borrowed = cursor.fetchall()
    print("Number of tools you borrowed: " + str(borrowed[0][0]))
    
    