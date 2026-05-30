from src.projectDL_1.components.data_validation import DataValidation
from src.projectDL_1.config.configuration import ConfigurationManager
from src.projectDL_1 import logger

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files()
            
        except Exception as e:
            raise e