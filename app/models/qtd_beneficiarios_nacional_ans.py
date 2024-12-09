from db import db
class Qtd_Beneficiarios_Nacional_Ans:
    def __init__(self):
        self.cursor = db.DB().cursor
        self.conn = db.DB().conn
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
        #self.conn.close()

    def insert_qtdbna(self, data_to_insert):
        self.cursor.executemany('''
            INSERT INTO qtd_beneficiarios_nacional_ans (
            ID_CMPT_MOVEL, CD_OPERADORA, NM_RAZAO_SOCIAL, SG_UF, 
            CD_MUNICIPIO, NM_MUNICIPIO, DE_CONTRATACAO_PLANO, QT_BENEFICIARIO_ATIVO
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data_to_insert)
        self.conn.commit()
        self.conn.close()

        self.conn.close()
