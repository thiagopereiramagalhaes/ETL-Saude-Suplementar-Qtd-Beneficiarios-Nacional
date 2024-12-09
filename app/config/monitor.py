import psutil
import os
import gc
from config import config

class Monitor_Memory:
    def __init__(self):
        self.limit_mb = config.Config().limit_mb
        
    def monitor_memory(self):
        process = psutil.Process(os.getpid())
        memory_used = process.memory_info().rss / (1024 * 1024)  # memória usada em MB
        gc.collect()
        if memory_used > self.limit_mb:
            print(f"Memória excedeu o limite de {self.limit_mb}MB. Liberando recursos...")
            os._exit(1) 
