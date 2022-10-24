def search(conn, cursor, param, type):
    records = None
    if type == 'barcode':
        cursor.execute(f"select * from tools_table where barcode={param}")
        records = cursor.fetchall()
    elif type == 'name':
        cursor.execute(f"select * from tools_table where tool_name={param}")
        records = cursor.fetchall()
    elif type == 'category':
        cursor.execute(f"select * from tools_table where type={param}")
        records = cursor.fetchall()
    return records