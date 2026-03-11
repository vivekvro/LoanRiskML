import streamlit as st
st.title("Loan Risk Prediction Project:")
st.markdown("""
### 📊 Loan Default Risk Prediction System

This application predicts the **risk of loan default** using a Machine Learning model trained on historical loan data.  
It analyzes borrower characteristics, financial indicators, and loan details to estimate the probability that a borrower may default.

---

### 📑 Application Pages

The application contains **two main pages available in the sidebar:**

#### 📝 User Input Page
- Allows users to enter **loan applicant details**.
- Includes borrower information, credit details, and loan parameters.
- After submission, the system predicts the **loan default risk** and stores the result.

#### 🔍 Loan Risk Lookup Page
- Users can **search using a User ID**.
- The system retrieves the previously evaluated record.
- Displays the **loan risk label and risk score** for that specific user.

---

### 🔎 How it Works
1. Enter borrower and loan information in the **User Input page**.
2. The data is processed and passed to the trained ML model.
3. The system returns:
   - **Risk Label** → Defaulter / Not Defaulter
   - **Risk Score** → Probability of default.
4. Users can later check the prediction using the **Loan Risk Lookup page**.

---

### 🧠 Model Details
- **Model:** Random Forest Classifier
- **Features:** Borrower demographics, credit score, loan attributes, and financial ratios.

---

### ⚠️ Disclaimer
This system is created for **educational and demonstration purposes only** and should not be used for real financial decision-making.
""")