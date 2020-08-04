import pickle
import sqlite3
from sqlite3 import Error

DATABASE_PATH = "users_database.db"

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_new_user(username, password):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (username, password))
    connection.commit()
    return True


def check_users_password(username, password):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM users WHERE (name,password) = (?, ?)", (username, password,))
    if data.fetchone():
        return True
    else:
        return False


con = create_connection("users_database.db")


# print(check_users_password(con, "admin", "admin"))
# create_new_user(con, "Петя", "123")

# query = '''CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   password TEXT);'''
# execute_query(con, query)
# user_1 = "INSERT INTO users (name, password) VALUES ('admin','admin')"
# execute_query(con, user_1)
# user_2 = "INSERT INTO users (name, password) VALUES ('use1r','use1r')"
# execute_query(con, user_2)
# cur = con.cursor()
# data = cur.execute("SELECT * FROM users WHERE name=?", ("admin",))
# print(data.fetchone())

class Database:
    def load_data(self):
        f = open('data.pickle', 'rb')
        massages_database = pickle.load(f)
        return massages_database

    def save_data(self, new_dat):
        massages_database = new_dat
        with open('data.pickle', 'wb') as f:
            pickle.dump(massages_database, f)
