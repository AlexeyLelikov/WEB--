import math
import time
import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
    
    def getMenu(self):
        sql = '''SELECT title,url FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            new_res = []
            for elem in res:
                new_res.append({"title": elem[0],"url": elem[1]})
            res = new_res
            if res: return res
        except:
            print("Ошибка чтения БД")
        return []
    
    def addPost(self, title , text):
        try:
            tm = int(math.floor(time.time()))
            self.__cur.execute("INSERT INTO posts VALUE(NULL,?,?,?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error:
            print("Ошибка довавления статьи в БД" + str(sqlite3.Error))
            return False
        return True
        

        
