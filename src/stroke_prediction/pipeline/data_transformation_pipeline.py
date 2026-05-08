from src.stroke_prediction.components.data_transformation import DataTransformation
from src.stroke_prediction.config.configuration import ConfiguartionManager
from src.stroke_prediction import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        print("Checking data validation status...")
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfiguartionManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                logger.info("Data validation failed. Data transformation will not proceed.")
        except Exception as e:
            logger.exception(e)
            print(e)

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.initiate_data_transformation()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        print(e)