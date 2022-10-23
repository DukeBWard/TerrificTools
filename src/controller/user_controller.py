from models.user_model import user_model

def login(cursor, user, password):
    cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchone()
    if records["username"] == user and records["pass"] == password:
        current_user = user_model(records["userid"], records["createdate"],records["lastaccess"], records["username"], records["pass"], records["email"], records["reqid"])
        print(current_user)
        return current_user
    else:
        return False
    