def login(cursor, user, password):
    cursor.execute(f"select * from user_table where username='{user}' and pass='{password}'")
    records = cursor.fetchall()
    print(records)