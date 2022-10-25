from models.request_ticket import request_ticket


def create_ticket(conn,cursor,user,date_needed,duration,barcode):
    cursor.execute(f"select * from tools_table where barcode= '{barcode}'")
    tool = cursor.fetchone()
    ownerid = tool["userid"]
    userid = user.userid
    if (tool["borrowed"] == True): 
        cursor.execute(f"insert into request_ticket_table(dateneeded, duration, status, barcode, userid, toolowner) values\
            ('{date_needed}', '{duration}', False, '{barcode}', '{userid}', '{ownerid}') ")
        conn.commit()
    else:
        return False
    

