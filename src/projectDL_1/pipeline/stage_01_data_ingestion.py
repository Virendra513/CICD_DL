from src.projectDL_1.components.data_ingestion import DataIngestion
from src.projectDL_1.config.configuration import ConfigurationManager
from src.projectDL_1 import logger

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e