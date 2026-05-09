from src.stroke_prediction.components.data_trainer import ModelTrainer
from src.stroke_prediction.config.configuration import ConfiguartionManager
from src.stroke_prediction import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config = ConfiguartionManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.initiate_model_trainer()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        print(e)