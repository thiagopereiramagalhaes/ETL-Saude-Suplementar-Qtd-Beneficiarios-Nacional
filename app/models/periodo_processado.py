from db import db

class Periodo_Processado:
    def __init__(self):
        # Inicializa conexão e cursor
        self.conn = db.DB().conn
        self.cursor = self.conn.cursor()
        # Cria a tabela se não existir
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

    def close_connection(self):
        # Fecha a conexão de forma segura
        if self.conn:
            self.conn.close()
    
    def get_last_date(self):
        try:
            self.cursor.execute('SELECT * FROM periodo_processado ORDER BY ano DESC, mes DESC, estado DESC LIMIT 1')
            last_date = self.cursor.fetchone()
            if last_date and last_date[2] == 'COMPLETO':  # Se o estado for COMPLETO
                return last_date[0] + 1  # Próximo ano
            elif last_date:  # Se não for COMPLETO
                return last_date[0]  # Ano atual
            else:  # Caso não haja registros
                return 2024
        except Exception as e:
            print(f"Erro ao buscar a última data: {e}")
            return 2024
        finally:
            self.close_connection()  # Garante o fechamento da conexão
    
    def insert_last_date(self, year, month, state, log):
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO periodo_processado (ano, mes, estado, log)
                VALUES (?, ?, ?, ?)
            ''', (year, month, state, str(log)))
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao inserir a última data: {e}")
        finally:
            self.close_connection()  # Garante o fechamento da conexão