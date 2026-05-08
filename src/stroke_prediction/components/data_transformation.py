import os
from src.stroke_prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.stroke_prediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        print("Performing train-test split...")
        
        data = pd.read_csv(self.config.data_path)
        train_data, test_data = train_test_split(data)

        train_data.to_csv(os.path.join(self.config.root_dir, "train.csv"),index=False)
        test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False)

        logger.info(f"Train and test data saved in {self.config.root_dir}")
        logger.info(f"Train data shape: {train_data.shape}")
        logger.info(f"Test data shape: {test_data.shape}")

        print(train_data.shape)
        print(test_data.shape)