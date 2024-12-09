import requests
import zipfile
import pandas as pd
import time
from tqdm import tqdm 
from io import BytesIO
from config.config import Config
from models.periodo_processado import Periodo_Processado as pp
from config.monitor import Monitor_Memory
from transform.transform import Transform

class Extract():
    def __init__(self):
        self.list_tasks = Config().list_tasks
        self.base_url = Config().base_url
        self.insert_last_date = pp().insert_last_date()
        self.monitor_memory = Monitor_Memory().monitor_memory()
        self.transform = Transform().transform()

    def extract(self):
        with tqdm(total=len(self.list_tasks), desc="Baixando dados", unit="dados") as pbar:
                for year, month, state in self.list_tasks:
                    url = f"{self.base_url}/{year}{month:02d}/pda-024-icb-{state}-{year}_{month:02d}.zip"
                    try:
                        response = requests.get(url, stream=True)
                        if response.status_code == 200:
                            with zipfile.ZipFile(BytesIO(response.content)) as z:
                                for file in z.namelist():
                                    if file.endswith('.csv'):

                                        with z.open(file) as csv_file:
                                            self.transform(csv_file, year, month, state)
                                            

                    except Exception as e:
                        print(f"Erro ao processar {url}: {e}")
                        self.insert_last_date(year, month, state, e)
                    
                    pbar.update(1)
                    time.sleep(3)
                    self.monitor_memory()