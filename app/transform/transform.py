import pandas as pd
from load import load
from config import monitor
import logging

class Transform:
    def __init__(self):
        self.monitor_memory = monitor.MonitorMemory()

    def read_csv(self, csv_file):
        try:
            dtypes = {
                "ID_CMPT_MOVEL": "str",
                "CD_OPERADORA": "str", 
                "NM_RAZAO_SOCIAL": "str", 
                "NR_CNPJ": "str", 
                "MODALIDADE_OPERADORA": "str", 
                "SG_UF": "str", 
                "CD_MUNICIPIO": "str", 
                "NM_MUNICIPIO": "str", 
                "TP_SEXO": "str", 
                "DE_FAIXA_ETARIA": "str", 
                "DE_FAIXA_ETARIA_REAJ": "str", 
                "DE_CONTRATACAO_PLANO": "str",
                "COBERTURA_ASSIST_PLAN": "str",
                "QT_BENEFICIARIO_ATIVO": "int64",
                "QT_BENEFICIARIO_ADERIDO": "int64",
                "QT_BENEFICIARIO_CANCELADO": "int64"
            }
            return pd.read_csv(
                csv_file,
                delimiter=';',
                encoding='utf-8',
                low_memory=False,
                dtype=dtypes
            )

        except pd.errors.ParserError as e:
            logging.error(f"Erro ao transformar dados: {e}")

    
    def init(self, csv_file, url):
        df_temp = self.read_csv(csv_file)
        columns_group = ['ID_CMPT_MOVEL',
                            'CD_OPERADORA', 
                            'NM_RAZAO_SOCIAL', 
                            'NR_CNPJ', 
                            'MODALIDADE_OPERADORA', 
                            'SG_UF', 
                            'CD_MUNICIPIO', 
                            'NM_MUNICIPIO', 
                            'TP_SEXO', 
                            'DE_FAIXA_ETARIA', 
                            'DE_FAIXA_ETARIA_REAJ', 
                            'DE_CONTRATACAO_PLANO',
                            'COBERTURA_ASSIST_PLAN'
                            ]
        columns_sum = [
            'QT_BENEFICIARIO_ATIVO',
            'QT_BENEFICIARIO_ADERIDO',
            'QT_BENEFICIARIO_CANCELADO'
        ]
            
        df_temp = df_temp[df_temp['COBERTURA_ASSIST_PLAN'] == 'Médico-hospitalar']
        df_temp = df_temp.groupby(columns_group, as_index=False)[columns_sum].sum()
        df_temp['ID_CMPT_MOVEL'] = df_temp['ID_CMPT_MOVEL'].str.replace('-', '', regex=False)

        
        self.monitor_memory.init()
        load.Load().init(df_temp, url)
        del df_temp
