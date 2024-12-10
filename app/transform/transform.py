import pandas as pd
from load import load
from config import monitor

class Transform:
    def __init__(self):
        self.monitor_memory = monitor.Monitor_Memory()

    def transform(self, csv_file, year, month, state):
        df_output = pd.DataFrame()
        df_temp = pd.read_csv(csv_file,delimiter=';', encoding='utf-8',dtype={'coluna_11': str}, low_memory=False)
        df_temp['Ano'] = year
        df_temp['Mes'] = month
        df_temp['Estado'] = state
        df_output = pd.concat([df_output, df_temp], ignore_index=True)
        df_output = df_output.groupby(['ID_CMPT_MOVEL', 'CD_OPERADORA', 'NM_RAZAO_SOCIAL', 'SG_UF', 'CD_MUNICIPIO', 'NM_MUNICIPIO', 'DE_CONTRATACAO_PLANO'])['QT_BENEFICIARIO_ATIVO'].sum().reset_index()


        load.Load().load(df_output, year, month, state)
        self.monitor_memory.monitor_memory()
