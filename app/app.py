from extract import extract as ext
import logging
from config import monitor
from config import config

class ConfigureLogging:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler(),  # Log na saída padrão
                logging.FileHandler("process.log")  # Log em arquivo
            ]
        )

class Main:
    def __init__(self):
        try:
            logging.info("Iniciando o processo de extração.")
            logging.info("Isso pode demorar um pouco!")
            logging.info(f"Consumo máximo de memória definido: {monitor.MonitorMemory().limit_mb}")
            logging.info(f"Requisição feita para: {config.Config().base_url}")
            
            ext.Extract().init()
            logging.info("Processo de extração concluído com sucesso.")
        except Exception as e:
            logging.error(f"Erro fatal durante a execução: {e}", exc_info=True)

if __name__ == "__main__":
    ConfigureLogging()
    Main()