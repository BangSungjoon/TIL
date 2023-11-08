import sqlite3
from library.dao import AbstractDAO

class ClientDAO(AbstractDAO):
    def getConnection(self):
        return sqlite3.connect('client.db')
