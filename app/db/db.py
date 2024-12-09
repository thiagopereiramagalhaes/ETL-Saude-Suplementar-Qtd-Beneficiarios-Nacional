import sqlite3

class _DB:
    def __init__(self):
        self.conn = sqlite3.connect('db.db') 
        self.cursor = self.conn.cursor()

class DB(_DB):
    def __init__(self):
        super().__init__()
