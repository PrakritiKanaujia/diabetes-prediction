# 🩺 Diabetes Prediction using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

## 📖 Overview

Diabetes is one of the most prevalent chronic diseases worldwide, affecting millions of people and placing a significant burden on healthcare systems. Early diagnosis enables timely treatment, reduces complications, and improves patient outcomes.

This project develops a **machine learning-based diabetes prediction system** that classifies whether an individual is likely to have diabetes using diagnostic health parameters. The trained model is deployed as an interactive **Streamlit web application**, allowing users to enter patient information and receive instant predictions.

The project demonstrates the complete machine learning workflow—from data preprocessing and model development to deployment as a user-friendly application.

---

## 🎯 Objectives

- Develop a binary classification model for diabetes prediction
- Perform data preprocessing and exploratory analysis
- Train and evaluate a machine learning model
- Serialize the trained model for deployment
- Build an interactive Streamlit application for real-time predictions

---

## 📊 Dataset

The project uses the **Pima Indians Diabetes Dataset**, a widely used benchmark dataset for binary classification problems in healthcare.

### Features

| Feature | Description |
|----------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| Diabetes Pedigree Function | Genetic predisposition score |
| Age | Age of the patient |

### Target Variable

- **0** → Non-diabetic
- **1** → Diabetic

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Jupyter Notebook

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| **mlModel.ipynb** | Jupyter notebook containing data preprocessing, model training, evaluation, and model serialization |
| **diabetes_app.py** | Streamlit application for interactive diabetes prediction |
| **diabetes.csv** | Dataset used for model development |
| **model_diabetes.sav** | Serialized machine learning model used by the application |
| **Diabetes_pred.pkl** | Additional saved model file |
| **README.md** | Project documentation |

---

## 🔄 Project Workflow

```text
Patient Dataset
       │
       ▼
Data Cleaning & Preprocessing
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Feature Selection
       │
       ▼
Train-Test Split
       │
       ▼
Machine Learning Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Model Serialization
       │
       ▼
Streamlit Web Application
       │
       ▼
Diabetes Prediction
```

---

## ⚙ Machine Learning Pipeline

The notebook follows the following workflow:

### 1. Data Loading

- Import dataset
- Inspect data structure
- Check for missing values

### 2. Data Preprocessing

- Prepare input features
- Separate target variable
- Split dataset into training and testing sets

### 3. Model Development

- Train the machine learning classifier
- Evaluate model performance
- Save the trained model using Pickle

### 4. Deployment

- Load the trained model
- Build an interactive user interface using Streamlit
- Generate predictions from user input

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/PrakritiKanaujia/diabetes-prediction.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch the Streamlit application

```bash
streamlit run diabetes_app.py
```

The application will open in your browser where you can enter patient information and receive predictions.

---

## 📈 Results

The trained machine learning model successfully predicts whether a patient is likely to have diabetes based on diagnostic measurements.

The Streamlit interface enables real-time predictions through a simple and intuitive user interface, making the model accessible to non-technical users.

---

## 💡 Skills Demonstrated

This project demonstrates practical experience in:

- Machine Learning
- Binary Classification
- Healthcare Data Analytics
- Data Preprocessing
- Model Evaluation
- Model Serialization
- Streamlit Application Development
- Python Programming

---

## 🔮 Future Improvements

Potential enhancements include:

- Compare multiple machine learning algorithms
- Hyperparameter optimization
- Cross-validation
- Explainable AI using SHAP or LIME
- Feature importance visualization
- Model deployment on Streamlit Community Cloud
- REST API implementation using FastAPI
- Docker containerization

---

## 📚 References

- Pima Indians Diabetes Dataset
- Scikit-learn Documentation
- Streamlit Documentation

---

## 📜 License

This project is intended for educational and learning purposes.

Feel free to use the code for academic and personal projects.
