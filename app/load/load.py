from models.periodo_processado import Periodo_Processado as pp
import pandas as pd


class Load:
    def __init__(self):
        self.insert_last_date = pp().insert_last_date()
        
    def load(self, df_output, year, month, state):
        output_path = "base_ans_qtd_beneficiarios_nacional.csv"
        df_output.to_csv(output_path, index = False)
        self.insert_last_date(year, month, state, 'COMPLETO')

        del csv_file
        del df_output
        self.monitor_memory()
