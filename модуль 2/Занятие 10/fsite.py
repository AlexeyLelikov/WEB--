import sqlite3 as sq
import os
from flask import Flask, render_template, request, g, flash, url_for
from FDataBase import FDataBase

# конфигурация
DATABASE = '/tmp/fsite.db'
DEBUG = True
SECRET_KEY = 'osrngserngosenvi4353489ht3fbe3490t2'
USERNAME = 'admin'
PASSWORD = '123'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'fsite.db')))

def connect_db():
    conn = sq.connect(app.config['DATABASE'])
    #conn.row_factory = sq.Row
    return conn

def create_db():
    """Вспомогательная функция для сосздания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g , 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    print(dbase.getMenu())
    return render_template("index.html", title = "Про Flask", menu = dbase.getMenu())

@app.route("/add_post", methods = ["POST" , "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        res = dbase.addPost(request.form['title'],request.form['post'])
        if res == False:
            flash('Ошибка добавления статьи')
        else:
            flash('Статья добавлена успешно')
    return render_template("add_post.html", title = "Добавление статьи", menu = dbase.getMenu())


if __name__ == "__main__":
    app.run(debug = True)