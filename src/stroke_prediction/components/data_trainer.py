import os
from src.stroke_prediction import logger
import pandas as pd
from xgboost import XGBClassifier
import joblib
from src.stroke_prediction.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        logger.info("Loading training data")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop(self.config.target_col, axis=1)
        test_x = test_data.drop(self.config.target_col, axis=1)
        train_y = train_data[self.config.target_col]
        test_y = test_data[self.config.target_col]

        lr = XGBClassifier(
            n_estimators=self.config.n_estimators,
            learning_rate=self.config.learning_rate,
            max_depth=self.config.max_depth,
            gamma=self.config.gamma,
            subsample=self.config.subsample,
            random_state=42
        )
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info("Model training completed and model is saved")
