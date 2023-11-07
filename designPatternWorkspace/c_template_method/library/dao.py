import sqlite3

class LibraryDAO:
    def create(self, sql):
        try:
            con = sqlite3.connect('template_method.db')
            cur = con.cursor()
            cur.execute(sql)
        finally:
            self.close(cur, con)
    
    def insert_many(self, sql, data):
        try:
            con = sqlite3.connect('template_method.db')
            cur = con.cursor()
            cur.executemany(sql, data)
            con.commit()
        except:
            con.rollback()
        finally:
            self.close(cur, con)

    def select(self, sql):
        try:
            con = sqlite3.connect('template_method.db')
            cur = con.cursor()
            cur.execute(sql)
            return cur.fetchall()
        finally:
            self.close(cur, con)

    def delete(self, sql):
        try:
            con = sqlite3.connect('template_method.db')
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except:
            con.rollback()
        finally:
            self.close(cur, con)

    def close(self, cur, con):
        cur.close()
        con.close()