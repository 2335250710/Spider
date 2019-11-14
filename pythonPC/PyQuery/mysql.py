import pymysql
# from test2 import *


class mysql(object):
    def __init__(self, host, user, password, database):
        self.db = pymysql.connect(host, user, password, database)
        self.cursor = self.db.cursor()

    def sql(self, sql, param):
        try:
            self.cursor.execute(sql, param)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def update(self, sql, param):
        return self.sql(sql, param)

    def delete(self, sql, param):
        return self.sql(sql, param)

    def insert(self, sql, param):
        return self.sql(sql, param)

    def get_one(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            self.cursor.close()
            self.db.close()

    def get_all(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def __repr__(self):
        return None

sql = "create table movies(mid int primary key auto_increment, grade int(10), title varchar(10), rate float(10))"
pc = mysql("localhost", "root", "123456", "pycharm")
