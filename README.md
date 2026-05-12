# Stroke Risk Prediction - End-to-End MLOps Pipeline
This project implements a modular, end-to-end Machine Learning pipeline to predict the probability of a patient suffering a stroke based on demographic and health metrics (Age, BMI, Hypertension, etc.).

## 🛠 Tech Stack

#### Language: Python 3.x

#### Framework: Flask (Web UI)

#### Machine Learning: XGBoost / Scikit-Learn

#### Tracking/Ops: MLflow & DVC (Data Version Control)

#### Frontend: HTML5 / CSS3 (Modern, responsive design)

## 🏗 ML Pipeline Workflows
The project is structured into five core modules. Every update is committed per module to ensure clean version control:

*Data Ingestion*: Fetching and loading the raw stroke dataset.

*Data Validation*: Checking the schema and data types to ensure data integrity.

*Data Transformation*: Handling categorical encoding (Gender, Smoking Status) and feature scaling.

*Model Trainer*: Training the XGBoost model and saving the serialized model.joblib.

*Model Evaluation*: Performance metrics logging and integration with MLflow.

### 🔄 Development Workflow (Step-by-Step)
To add a new feature or update a component, follow this specific order:

Update `config.yaml`: Define new paths or stage-specific configurations.

Update `schema.yaml`: Define column names and data types (Critical for Stroke data).

Update `params.yaml`: Adjust model hyperparameters (e.g., XGBoost learning rate).

Update the `Entity`: Define the return types for your configuration functions.

Update `Configuration Manager`: Located in src/config/configuration.py.

Update the `Components`: Write the actual logic (e.g., a new transformation step).

Update the `Pipeline`: Link the component to a pipeline stage.

Update `main.py`: Trigger the stage execution.

## 🚀 How to Run
1. Environment Setup
```bash
conda create -n stroke-prediction python=3.8 -y
conda activate stroke-prediction

pip install -r requirements.txt
```
2. Run the Full Pipeline
```bash
python main.py
```
3. Launch the Web App
```bash
python app.py

Then visit http://localhost:8080 in your browser.
```
🔗 Project Link
Check out the full repository here:
GitHub: Data-Science-Project-Stroke-Prediction