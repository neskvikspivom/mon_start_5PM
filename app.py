from flask import Flask


app = Flask(__name__)

from routes import *  # подключаю файл с маршрутизацией к сайту

if __name__ == '__main__':
    app.run()
