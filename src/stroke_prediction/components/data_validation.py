import os
import pandas as pd
from src.stroke_prediction import logger
from src.stroke_prediction.entity.config_entity import (DataIngestionConfig, DataValidationConfig)


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validated_status = True
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validated_status = False
                    logger.info(f"Data Validation Failed. Column: {col} is not in the schema.")
                    break

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validated_status}")

            return validated_status

        except Exception as e:
            raise e


    def validate_data_types(self) -> bool:
        try:
            validated_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_schema = self.config.all_schema

            for col in data.columns:
                if col in all_schema:
                    expected_dtype = all_schema[col]
                    actual_dtype = str(data[col].dtype)

                    if expected_dtype != actual_dtype:
                        validated_status = False
                        logger.info(f"Data Validation Failed. Column: {col} has dtype {actual_dtype} but expected {expected_dtype}.")
                        break
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validated_status}")
            return validated_status

        except Exception as e:
            raise e