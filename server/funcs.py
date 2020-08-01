import time
from models import Database
from models import check_users_password
from flask import request


def post_data():
    data = request.json
    username = data["username"]
    text = data["text"]
    massages_database = Database()
    nm = massages_database.load_data()
    nm["database"].append({"username": username, "text": text, "time": time.ctime()})
    massages_database.save_data(nm)
    return nm


def get_data():
    massages_database = Database().load_data()
    return massages_database


def checkpassword():
    data = request.json
    username = data["username"]
    passw = data["text"]
    return {"answer": check_users_password(username, passw)}


def passget():
    return "Everything is OK!"
