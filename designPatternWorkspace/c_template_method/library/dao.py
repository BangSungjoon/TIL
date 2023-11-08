from abc import ABCMeta, abstractmethod

class AbstractDAO(metaclass=ABCMeta):
    
    @abstractmethod
    def getConnection(self):pass
    
    def create(self, sql):
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.execute(sql)
        finally:
            self.close(cur, con)
            
    def insert_many(self, sql, data):
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.executemany(sql, data)
            con.commit()
        except:
            con.rollback()
        finally:
            self.close(cur, con)
            
    def select(self, sql):
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.execute(sql)
            return cur.fetchall()
        finally:
            self.close(cur, con)
            
    def delete(self, sql, data):
        try:
            con = self.getConnection()
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
    
            
    
