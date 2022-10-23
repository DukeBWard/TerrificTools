from models import user

def login(cursor, user, password):
    cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchone()
    if records["username"] == user and records["pass"] == password:
        user = user(records["userid"], records["createdate"], records["lastaccess"], records["username"], records["pass"], records["email"], records["reqid"])
        print(user)
        return user
    else:
        return False
    