Loan Approval Prediction
The goal of this project is to develop a predictive model to streamline loan approval processes. By leveraging machine learning techniques like Decision Trees, Random Forest, and Logistic Regression, the model aims to accurately predict loan approval outcomes. This will enable financial institutions to improve efficiency, reduce processing times, and enhance customer experiences.

Information About the Dataset:
The dataset consists of multiple features related to applicants and their financial and demographic information. These variables are used to determine the likelihood of loan approval.

There are 13 independent variables:

Loan_ID: Unique identifier for each loan application.
Gender: Gender of the applicant (Male/Female).
Married: Marital status of the applicant (Yes/No).
Dependents: Number of dependents the applicant has.
Education: Educational qualification of the applicant (Graduate/Undergraduate).
Self_Employed: Employment type (Self-Employed/Not Self-Employed).
ApplicantIncome: Applicant's monthly income.
CoapplicantIncome: Monthly income of the co-applicant (if applicable).
LoanAmount: Amount of loan requested (in thousands).
Loan_Amount_Term: Loan repayment duration (in months).
Credit_History: Record of the applicant's creditworthiness (meets guidelines or not).
Property_Area: Type of property area (Urban/Semi-Urban/Rural).
Target Variable:
Loan_Status: This is the outcome variable indicating whether the loan application was approved or not.
Animation of UI
Below is an animation demonstrating the user interface for the Loan Approval Prediction application:
Animated UI


Project Development Approach
Data Ingestion
In the Data Ingestion phase:

The data is first read as a CSV file.
The dataset is split into training and testing sets. Initial checks are performed to identify and handle null values and duplicate rows.
Rigorous exploratory data analysis (EDA) is conducted to gain insights into the data.
Feature Construction:
Customers are clustered based on their income, coapplicant income, credit history, dependents, and residential area.
A new column is created to estimate the risk probability of lending. This is calculated by subtracting the probability of approval in a cluster (ratio of approved loans in the cluster to total loans in the cluster) from 1.
Data Transformation
In the Data Transformation phase, the raw dataset is prepared for machine learning by applying several preprocessing steps:

1. Handling Numeric Data
The numerical columns ApplicantIncome, CoapplicantIncome, LoanAmount, and Loan_Amount_Term are preprocessed using the following steps:
Missing values are filled with the mean of the respective columns.
The values are scaled using Min-Max Scaling, which transforms the data to a range between 0 and 1 to normalize it for the model.
2. Imputing Credit History
For the Credit_History column, which has some missing values:
A K-Nearest Neighbors (KNN) Imputer is applied to estimate missing values. This method uses the similarity of neighboring data points to fill in the gaps.
The values are then scaled using Min-Max Scaling to standardize them.
3. Handling Categorical Data with Ordinal Encoding
For categorical columns like Dependents, Property_Area, and Education, which have a natural order:
Missing values are filled with the most frequent category.
The categories are encoded with Ordinal Encoding, which assigns a rank-based numeric value to each category. For example:
Dependents: "0", "1", "2", "3+" are encoded as 0, 1, 2, 3.
Property_Area: "Rural", "Semiurban", "Urban" are encoded in a specified order.
Education: "Not Graduate" and "Graduate" are encoded as 0 and 1, respectively.
4. Handling Categorical Data with One-Hot Encoding
For columns like Gender, Married, and Self_Employed that do not have a natural order:
Missing values are filled with the most frequent category.
These columns are then transformed using One-Hot Encoding, creating binary columns for each category. For instance:
If Gender has values "Male" and "Female," it creates one column (e.g., Gender_Male) with binary values (1 for Male, 0 for Female).
5. Combining All Preprocessing Steps
A ColumnTransformer is created to apply these transformations to the respective columns in one step:
The numerical columns are scaled after imputing missing values.
The Credit_History column is processed using KNN Imputation and scaling.
Ordinal encoding is applied to ordered categorical data.
One-Hot Encoding is applied to unordered categorical data.
6. Saving the Preprocessor
The entire preprocessing pipeline is saved as a pickle file for future use. This ensures that the same transformations can be applied consistently to new data during prediction.## Model Training
In this phase, multiple machine learning models were trained and evaluated to identify the best-performing one for predicting loan approval. The process involved the following steps:

1. Model Selection and Evaluation
Various machine learning models were tested and evaluated based on their performance metrics.
Gradient Boosting emerged as the best-performing model in terms of accuracy and reliability.
2. Hyperparameter Tuning
To further optimize the Gradient Boosting model, hyperparameter tuning was conducted.
The best hyperparameters identified were:
{
  "learning_rate": 0.2,
  "max_depth": 4,
  "n_estimators": 100
}
3. Model Saving
The trained Gradient Boosting model was serialized and saved as a pickle file for use in the prediction pipeline.
Prediction Pipeline
The Prediction Pipeline is designed to handle new input data, preprocess it, and generate predictions. The steps include:

1. Data Handling
The pipeline converts incoming data into a structured DataFrame format.
2. Loading Pre-trained Components
It loads the saved preprocessing pipeline and Gradient Boosting model from pickle files.
3. Generating Predictions
The input data is preprocessed using the loaded pipeline.
The preprocessed data is then fed into the Gradient Boosting model to produce predictions for loan approval.
This pipeline ensures consistent and efficient predictions for real-time data.
Flask App Creation
A Flask Web Application was developed to integrate the model into an accessible user interface. The features include:

1. User Interface
A simple and intuitive web interface where users can input the required features for loan prediction.
2. Loan Approval Prediction
On submitting the input, the Flask app utilizes the prediction pipeline to process the data and displays the predicted loan approval result.
This Flask app makes the loan approval prediction process available to end-users in a real-world scenario.
Usage:
conda create --name env python=3.11
conda activate env/
pip install -r requirements.txt
python app.py
Access http://localhost:5000/
