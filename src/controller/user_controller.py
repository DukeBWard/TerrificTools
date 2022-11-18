from re import L
from models.user_model import user_model

def login(conn, cursor, user, password):
    cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchone()
    if records["username"] == user and records["pass"] == password:
        userid = records["userid"]
        current_user = user_model(records["userid"], records["createdate"],records["lastaccess"], records["username"], records["pass"], records["email"], records["reqid"])
        cursor.execute(f"update user_table set lastaccess = CURRENT_DATE where userid ={userid}")
        conn.commit()   # NEED THIS TO UPDATE/INSERT CURRENT CHANGES
        return current_user
    else:
        return False

def signup(conn, cursor, user, password, email):
    cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchone()
    # Signup and login if not already signed up
    if records == None:
        cursor.execute(f"insert into user_table(createdate, lastaccess, username, pass, email) values\
            (CURRENT_DATE, CURRENT_DATE, '{user}', '{password}', '{email}') ")
        conn.commit()
        cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
        records = cursor.fetchone()
        if records["username"] == user and records["pass"] == password:
            userid = records["userid"]
            current_user = user_model(records["userid"], records["createdate"],records["lastaccess"], records["username"], records["pass"], records["email"], records["reqid"])
            cursor.execute(f"update user_table set lastaccess = CURRENT_DATE where userid ={userid}")
            conn.commit()   # NEED THIS TO UPDATE/INSERT CURRENT CHANGES
            return current_user
    # Log in if already signed up
    else:
        if records["username"] == user and records["pass"] == password:
            userid = records["userid"]
            current_user = user_model(records["userid"], records["createdate"],records["lastaccess"], records["username"], records["pass"], records["email"], records["reqid"])
            cursor.execute(f"update user_table set lastaccess = CURRENT_DATE where userid ={userid}")
            conn.commit()   # NEED THIS TO UPDATE/INSERT CURRENT CHANGES
            return current_user
    
def stats(conn, cursor, user):
    cursor.execute(f"select tools_table.tool_name, tools_table.barcode, count(request_ticket_table.barcode) \
    from request_ticket_table full outer join tools_table on request_ticket_table.barcode = tools_table.barcode where request_ticket_table.userid = {user.userid} \
    group by tools_table.barcode order by count(request_ticket_table.barcode) desc limit 10")
    records = cursor.fetchall()
    if records:
        for row in records:
                            print("Tool name: {}".format(row[0]))
                            print("Barcode: {}".format(row[1]))
                            print("Count: {}".format(row[2]))
                            print()
    else:
        print("You have not borrowed any tools.")
        print()
    print("Most Borrowed tools")
    cursor.execute(f"select tools_table.barcode, tools_table.tool_name, Sum(request_ticket_table.return_date - request_ticket_table.dateneeded)\
                    from request_ticket_table full outer join tools_table on request_ticket_table.barcode = tools_table.barcode where request_ticket_table.userid = {user.userid} and request_ticket_table.return_date is not null \
                   group by tools_table.barcode, request_ticket_table.dateneeded, request_ticket_table.return_date order by sum(request_ticket_table.return_date - request_ticket_table.dateneeded) desc limit 10")
    records = cursor.fetchall()
    if records:
        for row in records:
            print("Tool name: {}".format(row[0]))
            print("Barcode: {}".format(row[1]))
            print("Time: {}".format(row[2]))
            print()