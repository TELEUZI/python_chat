from flask import request

from server import app
import funcs
import time


@app.route("/status")
def status():
    dick = {
        'time': time.ctime(),
        'status': True
    }
    return dick


@app.route("/view")
def view():
    return funcs.get_data()


@app.route("/send", methods=['POST'])
def send():
    return funcs.post_data()


@app.route("/checkpass", methods=['POST', 'GET'])
def checkpass():
    if request.method == "POST":
        return funcs.checkpassword()
    else:
        return funcs.passget()

