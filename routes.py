from flask import render_template
from app import app  # импортирую главный модуль сайта


@app.route('/')  #  если перейти на главную страницу сайта
def main():  # вызовется функция
    return render_template('index.html')  # вернуть шаблон index.html

