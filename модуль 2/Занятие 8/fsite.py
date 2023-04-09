import sqlite3 as sq
import os
from flask import Flask, render_template, request

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
    conn.row_factory = sq.Row
    return conn

def create_db():
    """Вспомогательная функция для сосздания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()




