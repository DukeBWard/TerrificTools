from models.request_ticket import request_ticket


def create_ticket(conn,cursor,user,date_needed,duration,barcode):
    cursor.execute(f"select * from tools_table where barcode= '{barcode}'")
    tool = cursor.fetchone()
    ownerid = tool["userid"]
    userid = user.userid
    if (tool["availiable"] == True): 
        cursor.execute(f"insert into request_ticket_table(dateneeded, duration, status, barcode, userid, toolowner) values\
            ('{date_needed}', '{duration}', 'pending', '{barcode}', '{userid}', '{ownerid}') ")
        conn.commit()
    else:
        return False
    
def manage_incoming_tickets(conn, cursor, user):
    userid = user.userid
    cursor.execute(f"select * from request_ticket_table where toolowner= '{userid}'")
    requests = cursor.fetchall()
    print("---------------------")
    for row in requests:
        print("Request ID: {}".format(row[0]))
        print("Date needed: {}".format(row[1]))
        print("Duration: {}".format(row[2]))
        print("Current status: {}".format(row[3]))
        print("Tool barcode: {}".format(row[4]))
        print("Requested User: {}".format(row[5]))
        print("Return date: {}".format(row[7]))
        print("---------------------")

    reqid = input("Which request would you like to manage: ")
    cursor.execute(f"select toolowner from request_ticket_table where reqid='{reqid}'")
    toolowner = cursor.fetchone()
    cursor.execute(f"select status from request_ticket_table where reqid='{reqid}'")
    reqstatus = cursor.fetchone()
    if (toolowner[0] == userid and reqstatus == "pending"):
        status = input("Would you like to accept or deny request: ")
        if (status == "accept"):
            return_date = input("What should the return date be (yyyy-mm-dd): ")
            cursor.execute(f"select barcode from request_ticket_table where reqid= '{reqid}'")
            barcode = cursor.fetchone()
            cursor.execute(f"update request_ticket_table set status= 'accepted' where reqid= '{reqid}'")
            cursor.execute(f"update tools_table set available= '{False}' where barcode={barcode[0]}")
            cursor.execute(f"update request_ticket_table set return_date= '{return_date}' where barcode={barcode[0]}")
            conn.commit()

        elif (status == "deny"):
            cursor.execute(f"update request_ticket_table set status= 'denied' where reqid= '{reqid}'")
            conn.commit()


def manage_outgoing_tickets(conn, cursor, user):
    userid = user.userid
    cursor.execute(f"select * from request_ticket_table where userid= '{userid}'")
    requests = cursor.fetchall()
    print("---------------------")
    for row in requests:
        print("Request ID: {}".format(row[0]))
        print("Date needed: {}".format(row[1]))
        print("Duration: {}".format(row[2]))
        print("Current status: {}".format(row[3]))
        print("Tool barcode: {}".format(row[4]))
        print("Tool owner: {}".format(row[6]))
        print("Return date: {}".format(row[7]))
        print("---------------------")

    reqid = input("Which request would you like to manage: ")
    cursor.execute(f"select toolowner from request_ticket_table where reqid='{reqid}'")
    toolowner = cursor.fetchone()
    if (toolowner[0] == userid):
        status = input("Would you like to delete this request: ")
        if (status == "yes"):
            cursor.execute(f"delete from request_ticket_table where reqid= '{reqid}'")
            conn.commit()
    

# User should be able to return the tool they borrowed
# very similar to managing request tickets

def return_borrowed_tool(conn, cursor, user):
    userid = user.userid
    cursor.execute(f"select * from request_ticket_table where userid= '{userid}'")
    requests = cursor.fetchall()
    print("---------------------")
    for row in requests:
        print("Request ID: {}".format(row[0]))
        print("Date needed: {}".format(row[1]))
        print("Duration: {}".format(row[2]))
        print("Current status: {}".format(row[3]))
        print("Tool barcode: {}".format(row[4]))
        print("Requested User: {}".format(row[5]))
        print("Return date: {}".format(row[7]))
        print("---------------------")
    
    reqid = input("Which request would you like to manage: ")
    cursor.execute(f"select toolowner from request_ticket_table where reqid='{reqid}'")
    userid = cursor.fetchone()
    if (user.userid == userid[0]):
    
        status = input("Would you like to close the request and return the tool?: ")
        if (status == "yes"):
            
            # 1= change the req ticket, make availability == false YES
            cursor.execute(f"select barcode from request_ticket_table where reqid= '{reqid}'")
            barcode = cursor.fetchone()
            cursor.execute(f"update request_ticket_table set status= 'returned' where reqid= '{reqid}'")

            # 2- change tool, make available in tool == true YES
            cursor.execute(f"update tools_table set available= '{True}' where barcode={barcode[0]}")

            # 3- must store when the tool was returned but where? (ADDING IT TO THE REQUEST TICKET)
            
            # update the return date
            cursor.execute(f"update request_ticket_table set return_date= CURRENT_DATE where reqid= '{reqid}'")
            conn.commit()