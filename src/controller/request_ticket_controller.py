from models.request_ticket import request_ticket


def create_ticket(conn,cursor,user,date_needed,duration,barcode):
    cursor.execute(f"select * from tools_table where barcode= '{barcode}'")
    tool = cursor.fetchone()
    ownerid = tool["userid"]
    userid = user.userid
    if (tool["availiable"] == True): 
        cursor.execute(f"insert into request_ticket_table(dateneeded, duration, status, barcode, userid, toolowner) values\
            ('{date_needed}', '{duration}', False, '{barcode}', '{userid}', '{ownerid}') ")
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
        print("---------------------")

    reqid = input("Which request would you like to manage: ")
    cursor.execute(f"select toolowner from request_ticket_table where reqid='{reqid}'")
    toolowner = cursor.fetchone()
    if (toolowner[0] == userid):
        status = input("Would you like to accept or deny request: ")
        if (status == "accept"):
            cursor.execute(f"select barcode from request_ticket_table where reqid= '{reqid}'")
            barcode = cursor.fetchone()
            cursor.execute(f"update request_ticket_table set status= '{True}' where reqid= '{reqid}'")
            cursor.execute(f"update tools_table set availiable= '{False}' where barcode={barcode[0]}")
            conn.commit()

        elif (status == "deny"):
            cursor.execute(f"delete from request_ticket_table where reqid= '{reqid}'")
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
        print("---------------------")

    reqid = input("Which request would you like to manage: ")
    cursor.execute(f"select toolowner from request_ticket_table where reqid='{reqid}'")
    toolowner = cursor.fetchone()
    if (toolowner[0] == userid):
        status = input("Would you like to delete this request: ")
        if (status == "yes"):
            cursor.execute(f"delete from request_ticket_table where reqid= '{reqid}'")
            conn.commit()
    
