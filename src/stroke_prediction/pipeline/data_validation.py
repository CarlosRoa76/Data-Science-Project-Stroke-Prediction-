from src.stroke_prediction.components.data_validation import DataValidation
from src.stroke_prediction.config.configuration import ConfiguartionManager
from src.stroke_prediction import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfiguartionManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_data_types()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.initiate_data_validation()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e