from flask import Flask


app = Flask(__name__)

from routes import *  # подключаю файл с маршрутизацией к  __name__ == '__main__':сайту

if
    app.run()
