import joblib
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        # Load the training data header to map the exact columns XGBoost expects
        train_data = pd.read_csv(Path('artifacts/data_transformation/train.csv'))
        self.expected_columns = train_data.drop('stroke', axis=1).columns

    def predict(self, data):
        # 1. Convert the user's text input into dummy variables
        data_encoded = pd.get_dummies(data)
        
        # 2. Align it with the training columns (fills missing categories with 0)
        data_encoded = data_encoded.reindex(columns=self.expected_columns, fill_value=0)
        
        # 3. Make the prediction
        prediction = self.model.predict(data_encoded)
        return prediction