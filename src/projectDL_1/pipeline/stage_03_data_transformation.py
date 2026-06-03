from src.projectDL_1.config.configuration import ConfigurationManager
from src.projectDL_1.components.data_transformation import DataTransformation
from src.projectDL_1 import logger


class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        config=ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()