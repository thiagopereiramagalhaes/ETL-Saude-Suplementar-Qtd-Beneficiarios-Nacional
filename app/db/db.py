import sqlite3
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('D:/db.db') 
        self.cursor = self.conn.cursor()
