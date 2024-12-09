from datetime import datetime 
from models.periodo_processado import Periodo_Processado as pp

class Config:
    def __init__(self):
        self.limit_mb = 8000

        self.base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios-024"
        
        self.sysdate = datetime.now()
        
        self.now_year = self.sysdate.year
        
        self.now_month = self.sysdate.month
        
        self.list_years = range(pp().get_last_date(), self.now_year + 1)
        
        self.list_months = range(1,12 + 1)
        
        self.list_states = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", 
                            "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
        
        self.list_tasks = [
            (year, month, state) 
            for year in self.list_years 
            for month in (range(4, 12 + 1) if year == 2019 else range(1, 12 + 1) if year < self.now_year else range(1, self.now_month + 1)) 
            for state in self.list_states
        ]