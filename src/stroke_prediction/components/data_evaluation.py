import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import joblib
import mlflow.sklearn
from pathlib import Path
from urllib.parse import urlparse
from src.stroke_prediction.entity.config_entity import ModelEvaluationConfig
from src.stroke_prediction.utils.common import read_yaml, create_directories, save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        acc = accuracy_score(actual, pred)
        prec = precision_score(actual, pred)
        rec = recall_score(actual, pred)
        f1 = f1_score(actual, pred)
        return acc, prec, rec, f1

    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_col], axis=1)
        y_test = test_data[[self.config.target_col]]

        mlflow.set_tracking_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities = model.predict(X_test)

            (acc, prec, rec, f1) = self.eval_metrics(y_test, predicted_qualities)
            
            #saving metrics
            scores = {
                "accuracy": acc,
                "precision": prec,
                "recall": rec,
                "f1_score": f1
            }
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log the model
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("precision", prec)
            mlflow.log_metric("recall", rec)
            mlflow.log_metric("f1_score", f1)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="XGBoostStrokeModel")
            else:
                mlflow.sklearn.log_model(model, "model")