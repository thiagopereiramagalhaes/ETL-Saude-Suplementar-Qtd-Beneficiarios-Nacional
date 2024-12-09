import pandas as pd
from load.load import Load
from config.monitor import Monitor_Memory

class Transform:
    def __init__(self):
        self.monitor_memory = Monitor_Memory().monitor_memory()

    def transform(self, csv_file, year, month, state):
        df_output = pd.DataFrame()
        df_temp = pd.read_csv(csv_file,delimiter=';', encoding='utf-8',dtype={'coluna_11': str}, low_memory=False)
        df_temp['Ano'] = year
        df_temp['Mes'] = month
        df_temp['Estado'] = state
        df_output = pd.concat([df_output, df_temp], ignore_index=True)

        Load().load(df_output, year, month, state)
