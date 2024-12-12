from datetime import datetime 
import requests

class Config:
    def __init__(self):
        self.base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios-024"
                
                        
        self.list_states = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", 
                            "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]

        self.list_url = self.is_url_available()

    def is_url_available(self):
        list_url = []
        for year in range(2024,datetime.now().year+1):
            for month in range(1,12+1):
                for state in self.list_states:
                    if requests.head(f"{self.base_url}/{year}{month:02d}/").status_code == 200:
                        list_url.append(f"{self.base_url}/{year}{month:02d}/pda-024-icb-{state}-{year}_{month:02d}.zip")  
        
        return list_url