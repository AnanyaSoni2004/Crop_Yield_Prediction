# 🌾 Intelligent Crop Yield Prediction

An AI-based agricultural analytics system that predicts crop yield using soil, weather, and crop parameters.
Developed as part of **Project 8 – Intelligent Crop Yield Prediction & Agentic Farm Advisory**.

---

## 📌 Project Overview

This project focuses on designing a machine learning pipeline that predicts crop yield (tons per hectare) using environmental and soil conditions.

The system:

* Accepts structured farm input data
* Performs preprocessing (encoding + scaling)
* Applies classical ML models
* Evaluates model performance
* Displays predictions through a Streamlit-based UI

This represents **Milestone 1** of a larger agentic AI agricultural advisory system.

---

## 🎯 Problem Statement

Farm productivity depends on multiple environmental and soil factors.
This system predicts expected crop yield based on:

* Crop type
* Temperature
* Rainfall
* Humidity
* Sunlight
* Soil pH
* Soil nutrients (Nitrogen, Phosphorus, Potassium)
* Altitude
* Wind Speed

The goal is to support data-driven agricultural decisions.

---

## 🧠 Machine Learning Approach

### 🔹 Data Preprocessing

* Missing value handling
* One-Hot Encoding for crop type
* Feature scaling using StandardScaler
* Train-test split (80/20)

### 🔹 Models Implemented

* Linear Regression (Baseline)
* Decision Tree Regressor

### 🔹 Evaluation Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

### 📊 Model Comparison

Linear Regression outperformed the Decision Tree model, indicating predominantly linear relationships within the dataset.

---

## 📂 Dataset

* Source: Kaggle
* 30,000 rows
* Features include environmental, soil, and crop parameters
* Target: Crop Yield (tons/hectare)

---

## 🖥️ User Interface

Built using **Streamlit**.

The UI allows:

* Crop selection
* Adjustable environmental parameters (sliders)
* Soil parameter inputs
* Real-time yield prediction
* Yield category classification (Low / Medium / High)

---

## 🏗️ Project Structure

```
Crop_Yield_Prediction/
│
├── app.py                # Streamlit UI
├── model.py              # Model loading & prediction
├── train.py              # Model training script
├── model.pkl             # Trained Linear Regression model
├── encoder.pkl           # OneHotEncoder object
├── scaler.pkl            # StandardScaler object
├── crop_yield_dataset.csv
├── requirements.txt
└── GenAI_Capstone.ipynb  # Full ML workflow notebook
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Crop_Yield_Prediction.git
cd Crop_Yield_Prediction
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📈 Example Prediction

For:

* Crop: Wheat
* Rainfall: 120 mm
* Temperature: 25°C
* Soil pH: 6.5
* Nitrogen: 0.35%

Predicted Yield:
~22.17 tons/hectare
Category: Medium Yield
