import sqlite3
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('db.db') 
        self.cursor = self.conn.cursor()
