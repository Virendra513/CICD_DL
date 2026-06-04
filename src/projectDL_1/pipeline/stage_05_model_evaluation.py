from src.projectDL_1.config.configuration import ConfigurationManager
from src.projectDL_1.components.model_evaluation import ModelEvaluation
from src.projectDL_1 import logger



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()