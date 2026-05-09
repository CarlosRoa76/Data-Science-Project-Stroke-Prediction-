from src.stroke_prediction.components.data_evaluation import ModelEvaluation
from src.stroke_prediction.config.configuration import ConfiguartionManager
from src.stroke_prediction import logger
from pathlib import Path

STAGE_NAME = "Data Evaluation Stage"

class DataEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_data_evaluation(self):
        config = ConfiguartionManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_evaluation_pipeline = DataEvaluationPipeline()
        data_evaluation_pipeline.initiate_data_evaluation()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        print(e)