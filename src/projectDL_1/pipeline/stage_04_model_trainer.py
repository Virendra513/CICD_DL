from src.projectDL_1.config.configuration import ConfigurationManager
from src.projectDL_1.components.model_trainer import ModelTrainer
from src.projectDL_1 import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_Model_trainer_config()
        logger.info(f"Model trainer config: {model_trainer_config}")

        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

    