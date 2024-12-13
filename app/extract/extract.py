import requests
import zipfile
import pandas as pd
import time
import logging
from tqdm import tqdm 
from io import BytesIO
from config import config
from config import monitor
from transform import transform
from urllib3.exceptions import InsecureRequestWarning
import urllib3

class Extract:
    def __init__(self):
        self.list_url = config.Config().list_url
        self.base_url = config.Config().base_url
        self.monitor_memory = monitor.MonitorMemory()
        self.transform = transform.Transform()
        urllib3.disable_warnings(InsecureRequestWarning)

    def download_data(self, url):
        try:
            response = requests.get(url, stream=True, timeout=90, verify=False)
            response.raise_for_status()
            return BytesIO(response.content)
        except requests.RequestException as e:
            logging.error(f"Erro ao baixar os dados em: {url}. Motivo: {e}")

    def extract_and_process_zip(self, zip_content, url):
        try:
            with zipfile.ZipFile(zip_content) as z:
                for file in z.namelist():
                    if file.endswith('csv'):
                        with z.open(file) as csv_file:
                            self.transform.init(csv_file, url)
        except zipfile.BadZipFile as e:
            logging.error(f"Erro ao extrair dados: {e}")
        
    def init(self):
        with tqdm(total=len(self.list_url), desc="Baixando dados", unit="periodo/uf") as pbar:
            for url in self.list_url:
                zip_content = self.download_data(url)
                if zip_content:
                    self.extract_and_process_zip(zip_content, url)

                pbar.update(1)
                time.sleep(2)
                self.monitor_memory.init()