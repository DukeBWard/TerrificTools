def login(cursor, user, password):
    cursor.execute(f"select username,pass from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchone()
    if records["username"] == user and records["pass"] == password:
        return True
    else:
        return False
    