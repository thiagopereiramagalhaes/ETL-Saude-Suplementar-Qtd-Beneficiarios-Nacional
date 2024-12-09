from db.db import DB
class Periodo_Processado:
    def __init__(self):
        self.cursor = DB().conn
        self.conn = DB().cursor
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS periodo_processado (
                ano INTEGER,
                mes INTEGER,
                estado TEXT,
                log TEXT,
                PRIMARY KEY (ano, mes, estado)
            )
        ''')
        self.conn.commit()
        self.conn.close()
    
    def get_last_date(self):
            self.cursor.execute('SELECT * FROM periodo_processado ORDER BY ano DESC, mes DESC, estado DESC LIMIT 1')
            last_date = self.cursor.fetchone()
            self.conn.close()
            if last_date and last_date[2] == 'COMPLETO':
                return last_date[0] + 1
            elif last_date and last_date[2] != 'COMPLETO':
                return last_date[0]
            else:
                return 2019
    
    def insert_last_date(self,year, month, state, log):
        self.cursor.execute('''
            INSERT OR REPLACE INTO periodo_processado (ano, mes, estado, log)
            VALUES (?, ?, ?, ?)
        ''', (year, month, state, log))
        self.conn.commit()
        self.conn.close()