def search(conn, cursor, param, type):
    records = None
    if type == 'barcode':
        cursor.execute(f"select * from tools_table where barcode={param}")
        records = cursor.fetchall()
    elif type == 'name':
        cursor.execute(f"select * from tools_table where tool_name='{param}'")
        records = cursor.fetchall()
    elif type == 'category':
        cursor.execute(f"select * from tools_table where type='{param}'")
        records = cursor.fetchall()
    return records

def sort(conn, cursor, param, type):
    records = None
    if type == 'name' and param == "asc":
        cursor.execute(f"select * from tools_table order by tool_name asc")
        records = cursor.fetchall()
    elif type == 'name' and param == "desc":
        cursor.execute(f"select * from tools_table order by tool_name desc")
        records = cursor.fetchall()
    elif type == 'category' and param == "asc":
        cursor.execute(f"select * from tools_table order by type asc")
        records = cursor.fetchall()
    elif type == 'category' and param == "desc":
        cursor.execute(f"select * from tools_table order by type desc")
        records = cursor.fetchall()
    return records

def view(conn, cursor, type):
    #CURRENT_DATE
    if type == 'available':
        cursor.execute(f"select * from tools_table where available = '{True}' order by tool_name")
        order = cursor.fetchall()
    elif type == 'lent':
        cursor.execute(f"select  from request_ticket_table where toolowner = '' order by dateneeded ") #inner join via user id
        order = cursor.fetchall()
    elif type == 'borrowed':
        cursor.execute(f"select tools_table.tool_name, request_ticket_table.userid, request_ticket_table.toolowner  "
                       f"from tools_table where available = '{False}' inner join ")
        order = cursor.fetchall()
    return order