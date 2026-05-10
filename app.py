from flask import Flask, render_template, request
import os 
import pandas as pd
import numpy as np
from src.stroke_prediction.pipeline.data_prediction_pipeline import PredictionPipeline

# --- BULLETPROOF PATH LOGIC ---
# This finds the directory where app.py actually lives
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)
# ------------------------------

@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            age = float(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            avg_glucose_level = float(request.form['avg_glucose_level'])
            bmi = float(request.form['bmi'])
            gender = request.form['gender']
            ever_married = request.form['ever_married']
            work_type = request.form['work_type']
            residence_type = request.form['residence_type']
            smoking_status = request.form['smoking_status']
       
            # Creating a dictionary that matches the original dataset
            data_dict = {
                'gender': [gender],
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'ever_married': [ever_married],
                'work_type': [work_type],
                'Residence_type': [residence_type],
                'avg_glucose_level': [avg_glucose_level],
                'bmi': [bmi],
                'smoking_status': [smoking_status]
            }
            
            data_df = pd.DataFrame(data_dict)
            
            obj = PredictionPipeline()
            predict = obj.predict(data_df)

            # Format the output for the user
            result = "High Risk of Stroke" if predict[0] == 1 else "Low Risk of Stroke"

            return render_template('results.html', prediction=result)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong during prediction.'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)