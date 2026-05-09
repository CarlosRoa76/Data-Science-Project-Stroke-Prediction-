import os
from src.stroke_prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.stroke_prediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        #handling missing values
        data['bmi'] = data['bmi'].fillna(data['bmi'].median())

        #one hot encoding
        data = pd.get_dummies(data, columns=['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])
        
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

        train_data.to_csv(os.path.join(self.config.root_dir, "train.csv"),index=False)
        test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False)

        logger.info(f"Train and test data saved in {self.config.root_dir}")
        logger.info(f"Train data shape: {train_data.shape}")
        logger.info(f"Test data shape: {test_data.shape}")

        print(train_data.shape)
        print(test_data.shape)