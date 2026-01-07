
<h2>Heart Disease Prediction using Machine Learning</h2>

🧾Summary:

✅A machine learning model that predicts the likelihood of heart disease based on clinical and demographic health data.


📌 Overview

✅Cardiovascular diseases are among the leading causes of death worldwide. Early detection plays a critical role in prevention and treatment.
✅This project applies supervised machine learning algorithms to analyze patient health data and predict whether a person is likely to suffer from heart disease.

👉The project focuses on:

✅Data preprocessing and feature selection

✅Training and evaluating ML classification models

✅Interpreting model performance using appropriate metrics

❓ Problem Statement

✅Medical diagnosis often relies on multiple clinical factors, making manual assessment time-consuming and error-prone.
✅The objective of this project is to build an accurate and reliable ML model that can predict heart disease using patient health attributes such as age, cholesterol level, chest pain type, and exercise-induced angina.

📊 Dataset

✅Source: <a href="https://github.com/rajan-kumar-mu1439/heart-disease-prediction-ml/blob/main/heart%20disease%20dataset.csv">Heart disease Dataset</a>

🔑 Key Features

✅age – Age of the patient

✅sex – Gender (1 = male, 0 = female)

✅cp – Chest pain type

✅ – Resting blood pressure

✅chol – Serum cholesterol

✅thalach – Maximum heart rate achieved

✅oldpeak – ST depression

✅exang – Exercise-induced angina

🛠️ Tools & Technologies

✅Python, ✅NumPy, ✅Pandas, ✅Matplotlib / Seaborn, ✅Scikit-learn

Environment: Jupyter Notebook


⚙️ Methodology

✅Data loading and inspection

✅Handling missing values

✅Feature selection

✅Data standardization

✅Train-test split

✅Model training (Logistic Regression / Random Forest)

✅Model evaluation using classification metrics


📈 Key Insights

✅Certain features like chest pain type, maximum heart rate, and oldpeak have strong correlation with heart disease.

✅Standardization significantly improves model performance.

✅Accuracy alone is not sufficient; precision and recall provide better evaluation for medical datasets.

🖥️ Model / Output

👉Model Used: Logistic Regression 

👉Evaluation Metrics:

✅Accuracy

✅Precision

✅Confusion Matrix

📊 Result Example

Accuracy: ~85% 

▶️ How to Run This Project
# Clone the repository
git clone https://github.com/rajan-kumar-mu1439/heart-disease-prediction-ml.git

# Navigate to project directory
cd heart-disease-prediction-ml

# Install dependencies
pip install -python, numpy, pandas, matplotlib, seaborn, scikit learn

# Open Jupyter Notebook
jupyter notebook


👉Then run Heart_disease_predict.ipynb.

📊 Results & Conclusion

✅The trained model successfully predicts the presence of heart disease with reasonable accuracy.

✅This demonstrates that machine learning can assist healthcare professionals by providing a data-driven decision support tool.


🔮 Future Work

✅Use ensemble models (Random Forest, XGBoost)

✅Perform hyperparameter tuning

✅Handle class imbalance using SMOTE

✅Deploy the model using Streamlit or Flask

✅Add explainability (SHAP / feature importance)


👤 Author & Contact

Rajan kumar

GitHub: https://github.com/rajankumar-1439

LinkedIn: https://www.linkedin.com/in/rajan-kumar-mu1439/

Email: rajankumarmu1439@gmail.com
