from src.stroke_prediction.components.data_ingestion import DataIngestion
from src.stroke_prediction.config.configuration import ConfiguartionManager
from src.stroke_prediction import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfiguartionManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e