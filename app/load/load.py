from models import qtd_beneficiarios_nacional_ans
from config import monitor
import logging

class Load:
    def __init__(self, output_path="base_ans_qtd_beneficiarios_nacional.csv"):
        self.insert_qtdbna = qtd_beneficiarios_nacional_ans.QtdBeneficiariosNacionalAns()
        self.monitor_memory = monitor.MonitorMemory()
        self.output_path = output_path

    def save_to_csv(self, df, path=None, activate = False):
        if activate:
            if path is None:
                path = self.output_path

            try:
                df.to_csv(path, index=False, sep=';')

            except Exception as e:
                logging.error(f"Erro ao salvar: {path}. Motivo: {e}")

    def insert_into_db(self, data_to_insert):
            self.insert_qtdbna(data_to_insert)

    def init(self, df_output, url):
        try:
            self.save_to_csv(df_output, f"{df_output['SG_UF'][0]}{df_output['ID_CMPT_MOVEL'][0]}.csv" )
            self.insert_qtdbna.insert_data_into_db(df_output.values.tolist())
            #logging.info(f"{url}: Carregado com sucesso.")
        except Exception as e:
            logging.error(f"{url}: Falha ao carregar. Motivo: {e}")
        
        del df_output
        self.monitor_memory.init()