from models import periodo_processado
from models import qtd_beneficiarios_nacional_ans
from config import monitor

class Load:
    def __init__(self):
        self.insert_last_date = periodo_processado.Periodo_Processado()
        self.insert_qtdbna = qtd_beneficiarios_nacional_ans.Qtd_Beneficiarios_Nacional_Ans()
        self.monitor_memory = monitor.Monitor_Memory()

    def load(self, df_output, year, month, state):
        output_path = "base_ans_qtd_beneficiarios_nacional.csv"
        df_output.to_csv(output_path, index = False)

        data_to_insert = df_output[['ID_CMPT_MOVEL', 'CD_OPERADORA', 'NM_RAZAO_SOCIAL', 'SG_UF', 'CD_MUNICIPIO', 'NM_MUNICIPIO', 'DE_CONTRATACAO_PLANO', 'QT_BENEFICIARIO_ATIVO']].values.tolist()

        self.insert_qtdbna.insert_qtdbna(data_to_insert)

        #self.insert_last_date.insert_last_date(year, month, state, 'COMPLETO')
        del df_output
        self.monitor_memory.monitor_memory()
