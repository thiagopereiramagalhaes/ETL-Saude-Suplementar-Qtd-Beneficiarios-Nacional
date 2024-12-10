from db import db

class Qtd_Beneficiarios_Nacional_Ans:
    def __init__(self):
        # Inicializa conexão e cursor
        self.conn = db.DB().conn
        self.cursor = self.conn.cursor()
        # Cria a tabela se não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS qtd_beneficiarios_nacional_ans (
                ID_CMPT_MOVEL INTEGER,
                CD_OPERADORA INTEGER,
                NM_RAZAO_SOCIAL TEXT,
                SG_UF TEXT,
                CD_MUNICIPIO TEXT,
                NM_MUNICIPIO TEXT,
                DE_CONTRATACAO_PLANO TEXT,
                QT_BENEFICIARIO_ATIVO INTEGER
            )
        ''')
        self.conn.commit()

    def close_connection(self):
        # Fecha a conexão de forma segura
        if self.conn:
            self.conn.close()

    def insert_qtdbna(self, data_to_insert):
        try:
            # Valida se os dados estão no formato esperado (lista de tuplas)
            if not isinstance(data_to_insert, list) or not all(isinstance(row, tuple) for row in data_to_insert):
                raise ValueError("Os dados devem ser uma lista de tuplas.")
            
            self.cursor.executemany('''
                INSERT INTO qtd_beneficiarios_nacional_ans (
                    ID_CMPT_MOVEL, CD_OPERADORA, NM_RAZAO_SOCIAL, SG_UF, 
                    CD_MUNICIPIO, NM_MUNICIPIO, DE_CONTRATACAO_PLANO, QT_BENEFICIARIO_ATIVO
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', data_to_insert)
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao inserir os dados: {e}")
        finally:
            self.close_connection()  # Garante que a conexão seja fechada
