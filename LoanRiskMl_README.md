# Loan Risk Prediction System

## Overview

The **Loan Risk Prediction System** is a Machine Learning application designed to predict whether a loan applicant is likely to **default or not default** based on financial and demographic features.

The project demonstrates a **complete ML application pipeline**, including:

* Data preprocessing and feature engineering
* Model training
* API-based prediction service
* Database storage
* Interactive frontend dashboard

The system uses a trained **Random Forest model** to estimate loan default risk and exposes the model through a **FastAPI backend**, which is consumed by a **Streamlit frontend**.

---

# Project Architecture

```
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
Machine Learning Model
        │
        ▼
MySQL Database
```

This architecture reflects how **production ML systems** are typically deployed.

---

# Project Structure

```
PROJECT 4
│
├── data
│   └── Cleaned_loan_records.csv
│
├── models
│   └── rf
│       └── LoanDefaulterPredictor.pkl
│
├── pages
│   └── 1_UserDetails.py
│
├── src
│   │
│   ├── core
│   │   ├── predictor.py
│   │   └── routes.py
│   │
│   ├── data
│   │   ├── curd.py
│   │   ├── engine.py
│   │   └── tables.py
│   │
│   └── schemas
│       └── schemas.py
│
├── transformers
│
├── app.py
│
├── Modeling.ipynb
├── dataclean.ipynb
├── Overview.ipynb
│
├── requirements.txt
├── .env
└── README.md
```

---

# Features

### Loan Risk Prediction

Predict whether a loan applicant is a **Defaulter** or **Not Defaulter**.

### Database Storage

Stores:

* User loan application records
* Prediction results

### API Endpoints

FastAPI provides endpoints for:

* Inserting loan records
* Generating predictions
* Searching records by user ID

### Interactive UI

Streamlit dashboard allows users to:

* Input loan details
* Generate predictions
* Search records

---

# Machine Learning Model

Model used:

```
Random Forest Classifier
```

Prediction output:

```
Prediction: 0 → Not Defaulter
Prediction: 1 → Defaulter
```

The system also returns a **risk score**, representing the probability of loan default.

Example output:

```
{
"id": 1023,
"label": "Defaulter",
"prediction": 1,
"risk_score": 0.81
}
```

---

# Installation

## 1 Clone the repository

```
git clone <repo-url>
cd project
```

## 2 Create virtual environment

```
python -m venv myenv
```

## 3 Activate environment

Windows:

```
myenv\Scripts\activate
```

## 4 Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

## Start FastAPI backend

```
python -m uvicorn src.core.routes:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit dashboard

```
streamlit run app.py
```

---

# API Endpoints

### Insert Record

```
POST /insertrecord
```

Stores user information and generates prediction.

---

### Get User Record

```
GET /getUserrecord/{user_id}
```

Returns user loan details.

---

### Get Prediction

```
GET /getLoanriskrecord/{user_id}
```

Returns prediction result.

---

# Dataset

Dataset used:

```
Cleaned_loan_records.csv
```

Contains loan applications with features such as:

* Loan amount
* Interest rate
* Credit score
* Income
* Property value
* Loan term
* Debt-to-income ratio
* Loan-to-value ratio
* Region
* Occupancy type

These features help determine **loan default risk**.

---

# Future Improvements

Possible improvements include:

* Model monitoring and logging
* Docker containerization
* Cloud deployment
* Feature store integration
* Model version tracking

---

# Author

**Vivek Singh**

BCA Student – IGNOU
Interested in Machine Learning, Data Science, and AI Engineering.

---

# License

This project is developed for **educational and demonstration purposes**.
