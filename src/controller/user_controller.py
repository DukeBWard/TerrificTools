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
    cursor.execute(f"insert into user_table(createdate, lastaccess, username, pass, email) values\
        (CURRENT_DATE, CURRENT_DATE, '{user}', '{password}', '{email}') ")
    conn.commit()
    return True

    