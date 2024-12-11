from db import database
import sqlite3
import logging


class QtdBeneficiariosNacionalAns:
    def __init__(self, db_path='db.db'):
        self.db_path = db_path
        with database.DataBase(self.db_path) as db:
            db.execute_query('''
                CREATE TABLE IF NOT EXISTS qtd_beneficiarios_nacional_ans (
                    ID_CMPT_MOVEL,
                    CD_OPERADORA, 
                    NM_RAZAO_SOCIAL, 
                    NR_CNPJ, 
                    MODALIDADE_OPERADORA, 
                    SG_UF, 
                    CD_MUNICIPIO, 
                    NM_MUNICIPIO, 
                    TP_SEXO, 
                    DE_FAIXA_ETARIA, 
                    DE_FAIXA_ETARIA_REAJ, 
                    DE_CONTRATACAO_PLANO,
                    COBERTURA_ASSIST_PLAN,
                    QT_BENEFICIARIO_ATIVO,
                    QT_BENEFICIARIO_ADERIDO,
                    QT_BENEFICIARIO_CANCELADO
                )
            ''')
    def insert_data_into_db(self, data_to_insert):
        query = '''
            INSERT INTO qtd_beneficiarios_nacional_ans (
                    ID_CMPT_MOVEL,
                    CD_OPERADORA, 
                    NM_RAZAO_SOCIAL, 
                    NR_CNPJ, 
                    MODALIDADE_OPERADORA, 
                    SG_UF, 
                    CD_MUNICIPIO, 
                    NM_MUNICIPIO, 
                    TP_SEXO, 
                    DE_FAIXA_ETARIA, 
                    DE_FAIXA_ETARIA_REAJ, 
                    DE_CONTRATACAO_PLANO,
                    COBERTURA_ASSIST_PLAN,
                    QT_BENEFICIARIO_ATIVO,
                    QT_BENEFICIARIO_ADERIDO,
                    QT_BENEFICIARIO_CANCELADO
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        with database.DataBase(self.db_path) as db:
            try:
                db.cursor.executemany(query, data_to_insert)
                db.conn.commit()
            except sqlite3.IntegrityError as e:
                logging.error(f"Erro ao gravar dados em: qtd_beneficiarios_nacional_ans. Motivo: {e}")
            except sqlite3.Error as e:
                logging.error(f"Erro ao gravar dados em: qtd_beneficiarios_nacional_ans. Motivo: {e}")