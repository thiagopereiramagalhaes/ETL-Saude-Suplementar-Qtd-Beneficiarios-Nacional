import pandas as pd
from load import load
from config import monitor
import logging

class Transform:
    def __init__(self):
        self.monitor_memory = monitor.MonitorMemory()

    def read_csv(self, csv_file):
        try:
            return pd.read_csv(
                csv_file,
                delimiter=';',
                encoding='utf-8',
                low_memory=False
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
        self.monitor_memory.init()
        load.Load().init(df_temp, url)
        del df_temp
