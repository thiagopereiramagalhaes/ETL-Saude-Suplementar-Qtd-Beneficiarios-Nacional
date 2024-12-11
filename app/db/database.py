import sqlite3
import logging

class DataBase:
    def __init__(self, db_path='db.db'):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path) 
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            self.conn.commit()

        except sqlite3.Error as e:
            logging.error(f"Erro durante a gravação do registro no banco: {e}")

        return None