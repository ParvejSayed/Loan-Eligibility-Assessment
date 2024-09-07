from flask import Flask, render_template, request
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.pipeline.prediction_pipeline import predictionPipeline, customClass
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def prediction_data():
    if request.method == "GET":
        return render_template("home.html")
    else:
        try:
            logging.info("Form data received")
            data = customClass(
                Gender=request.form.get("Gender"),
                Married=request.form.get("Married"),
                Dependents=request.form.get("Dependents"),
                Education=request.form.get("Education"),
                Self_Employed=request.form.get("Self_Employed"),
                ApplicantIncome=int(request.form.get("ApplicantIncome")),
                CoapplicantIncome=float(request.form.get("CoapplicantIncome")),
                LoanAmount=float(request.form.get("LoanAmount")),
                Loan_Amount_Term=float(request.form.get("Loan_Amount_Term")),
                Credit_History=float(request.form.get("Credit_History")),
                Property_Area=request.form.get("Property_Area")
            )

            logging.info("Custom class instance created successfully")

            final_data = data.get_data_frame()
            logging.info(f"Data frame created: {final_data}")

            prediction_func = predictionPipeline()
            pred = prediction_func.predict(final_data)
            logging.info(f"Prediction result: {pred}")

            result = pred[0]

            if result == 0:
                final_result = '''Sorry,Your Loan is Not APPROVED, 
                better Luck Next Time!'''
            else:
                final_result = "Congrats, Your Loan is APPROVED"

            return render_template("home.html", final_result=final_result)
        
        except Exception as e:
            logging.exception("An error occurred during prediction.")
            return render_template("home.html", final_result="An error occurred during prediction. Please try again later.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

