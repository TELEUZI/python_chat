import time
from models import Database, create_new_user
from models import check_users_password, create_new_user
from flask import request


def post_data():
    data = request.json
    username = data["username"]
    text = data["text"]
    time = data["time"]
    massages_database = Database().load_data()
    massages_database.append({"username": username, "text": text, "time": time})
    massages_database.save_data()
    return {"database": nm}


def get_data():
    massages_database = Database().load_data()
    return {"database": massages_database}


def checkpassword():
    data = request.json
    username = data["username"]
    passw = data["text"]
    return {"answer": check_users_password(username, passw)}


def passget():
    return "Everything is OK!"


def create_user():
    data = request.json
    username = data["username"]
    passw = data["text"]
    return {"answer": create_new_user(username, passw)}
