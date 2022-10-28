def create_category(conn, cursor):
    user_input = input("Category Name: ")
    cursor.execute(f"select * from category_table where category='{user_input}'")
    category = cursor.fetchone()
    if category is None:
        cursor.execute(f"insert into category_table(category) values\
                ('{user_input}') ")
        conn.commit()
        return category
    else:
        print("That category already exists")
        return None


def search_category(conn, cursor):
    category = input("Category Name: ")
    cursor.execute(f"select * from category_table where category='{category}'")
    category = cursor.fetchone()
    if category is None:
        print("This category does not exist. Please create this category")
        category = create_category(conn, cursor)
    return category


