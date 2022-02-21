from flask import render_template
from app import app  # импортирую главный модуль сайта


@app.route('/')  #  если перейти на главную страницу сайта
def main():  # вызовется функция
    return render_template('index.html')  # вернуть шаблон index.html


@app.route('/contacts')  # если перейти на страницу contacts
def contacts():
    return render_template('contacts.html')


@app.route('/about')
def about():
    return render_template('about.html')

