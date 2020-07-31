from flask import Flask, request, render_template, flash
import time
import pickle

app = Flask(__name__)
app.secret_key = "hell"
f = open('data.pickle', 'rb')
massages_database = pickle.load(f)


@app.route("/")
def homepage():
    return render_template("index.html", name = "bustard")


@app.route("/status")
def status():
    dick={
        'time' : time.ctime(),
        'status' : True
    }
    return dick


@app.route("/view")
def view():
    return {"massages_for_receiving": massages_database}


@app.route("/send", methods=['POST', 'GET'])
def send():
    if request.method == "POST":
        data = request.json
        username = data["username"]
        text = data["text"]
        massages_database.append({"username": username, "text": text, "time": time.ctime()})
        with open('data.pickle', 'wb') as f:
            pickle.dump(massages_database, f)
        return "+"
    else:
        return {"massages_for_receiving": massages_database}


app.run(debug = False)
