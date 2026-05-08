from src.stroke_prediction import logger
from src.stroke_prediction.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.stroke_prediction.pipeline.data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e