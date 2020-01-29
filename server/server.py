from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    dick={
        'time' : time.ctime(),
        'status' : True
    }
    return dick


@app.route("/send")
def send():
    return None


app.run()