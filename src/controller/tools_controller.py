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
    order = None
    if type == 'available':
        cursor.execute(f"select * from tools_table where available = '{True}' order by tools_name")
        order = cursor.fetchall()
    elif type == 'lent':
        # cursor.exceute(f"select tools_table.userid,  from tools_table where available = '{False}' and userid = ") #inner join via user id
        order = cursor.fetchall()
    elif type == 'borrowed':
       # cursor.exceute(f"select * from tools_table where available = '{False}'")
        order = cursor.fetchall()
    return order