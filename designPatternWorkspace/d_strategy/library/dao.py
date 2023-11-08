from abc import ABCMeta, abstractmethod

class LibrarytDAO(metaclass=ABCMeta):
    
    def __init__(self, con_creator):
        self.con_creator = con_creator
    
    def create(self, sql):
        try:
            con = self.con_creator.getConnection()
            cur = con.cursor()
            cur.execute(sql)
        finally:
            self.close(cur, con)
            
    def insert_many(self, sql, data):
        try:
            con = self.con_creator.getConnection()
            cur = con.cursor()
            cur.executemany(sql, data)
            con.commit()
        except:
            con.rollback()
        finally:
            self.close(cur, con)
            
    def select(self, sql):
        try:
            con = self.con_creator.getConnection()
            cur = con.cursor()
            cur.execute(sql)
            return cur.fetchall()
        finally:
            self.close(cur, con)
            
    def delete(self, sql, data):
        try:
            con = self.con_creator.getConnection()
            cur = con.cursor()
            cur.execute(sql, data)
            con.commit()
        except:
            con.rollback()
        finally:
            self.close(cur, con)
    
    def close(self, cur, con):
        cur.close()
        con.close()
    
            
    
