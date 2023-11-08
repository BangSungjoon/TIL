import sqlite3
from library.abstractConnectionCreator import AbstractConnectionCreator

class ConnectionCreator(AbstractConnectionCreator):
    def getConnection(self):
        return sqlite3.connect('strategy.db')
    