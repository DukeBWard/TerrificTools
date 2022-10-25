from models.request_ticket import request_ticket


def create_ticket(conn,cursor,user,date_needed,duration,barcode):
    cursor.execute(f"select * from tools_table where barcode= '{barcode}'")
    tool = cursor.fetchone()
    userid = user.userid
    if (tool["borrowed"] == True): 
        cursor.execute(f"insert into request_ticket_table(dateneeded, duration, status, barcode, userid) values\
            ('{date_needed}', '{duration}', False, '{barcode}', '{userid}') ")
        conn.commit()
        cursor.execute(f"select * from request_ticket_table where barcode = '{barcode}'")
        records = cursor.fetchone()
        reqid = records["reqid"]
        cursor.execute(f"update user_table set reqid = {reqid} where userid = {userid}") # Might delete reqid from user table
        conn.commit
    else:
        return False
    

