def receiver():
    import requests
    massages = requests.get("HTTP://127.0.0.1:5000/send").json()["massages_for_receiving"]

    for massage in massages:
            print(massage["username"], massage["text"], massage["time"])


def sender():
    import requests
    import time

    username = input("Введите своё имя")

    while True:
        text = input()
        requests.post("http://127.0.0.1:5000/send", json = {"username": username, "text": text, "time": time.ctime()})