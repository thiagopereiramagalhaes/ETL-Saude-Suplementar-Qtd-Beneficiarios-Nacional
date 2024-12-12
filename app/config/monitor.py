import psutil
import os
import gc
import logging


class MonitorMemory:
    def __init__(self, limit_mb=5000, terminate_on_exceed=True):
        self.limit_mb = limit_mb
        self.terminate_on_exceed = terminate_on_exceed


    def set_memory_limit(self, limit_mb):
        self.limit_mb = limit_mb

    def get_memory_usage(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / (1024 * 1024)
    
    def init(self):
        memory_used = self.get_memory_usage()

        gc.collect()
        if memory_used > self.limit_mb:
            if self.terminate_on_exceed:
                logging.error(f"Memória máxima atingida: {memory_used}", exc_info=True)
                os._exit(1)