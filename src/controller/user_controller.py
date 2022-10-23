from models import user

def login(cursor, user, password):
    cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchone()
    print(records)
    if records["username"] == user and records["pass"] == password:
        current_user = user(records["userid"], None,None, records["username"], records["pass"], records["email"], records["reqid"])
        print(current_user)
        return True
    else:
        return False
    