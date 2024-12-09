from models.periodo_processado import Periodo_Processado as pp
from models.qtd_beneficiarios_nacional_ans import Qtd_Beneficiarios_Nacional_Ans as qtdbna

class Load:
    def __init__(self):
        self.insert_last_date = pp().insert_last_date()
        self.insert_qtdbna = qtdbna().insert_qtdbna()

    def load(self, df_output, year, month, state):
        output_path = "base_ans_qtd_beneficiarios_nacional.csv"
        df_output.to_csv(output_path, index = False)

        self.insert_qtdbna(df_output['ID_CMPT_MOVEL'], df_output['CD_OPERADORA'], df_output['NM_RAZAO_SOCIAL'], df_output['SG_UF'], df_output['CD_MUNICIPIO'], df_output['NM_MUNICIPIO'], df_output['DE_CONTRATACAO_PLANO'], df_output['QT_BENEFICIARIO_ATIVO'])

        self.insert_last_date(year, month, state, 'COMPLETO')
        del csv_file
        del df_output
        self.monitor_memory()