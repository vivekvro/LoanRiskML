import pandas as pd
from src.schemas.schemas import UserRecord
import sys
sys.path.append("../../")
from joblib import load
predictor = load("../../models/rf/LoanDefaulterPredictor_100326_v1.joblib")


def get_prediction(user:UserRecord):
    model=predictor
    input = pd.DataFrame({
        'loan_limit':user.loan_limit,
        'Gender':user.gender,
        'approv_in_adv':user.approv_in_adv,
        'loan_type':user.loan_type,
        'loan_purpose':user.loan_purpose,
        'Credit_Worthiness':user.credit_worthiness,
        'open_credit':user.open_credit,
        'business_or_commercial':user.business_or_commercial,
        'loan_amount':user.loan_amount,
        'rate_of_interest':user.rate_of_interest,
        'Upfront_charges':user.upfront_charges,
        'term':user.term,
        'Neg_ammortization':user.neg_ammortization,
        'interest_only':user.interest_only,
        'lump_sum_payment':user.lump_sum_payment,
        'property_value':user.property_value,
        'construction_type':user.construction_type,
        'occupancy_type':user.occupancy_type,
        'Secured_by':user.secured_by,
        'total_units':user.total_units,
        'income':user.income,
        'credit_type':user.credit_type,
        'Credit_Score':user.credit_score,
        'co-applicant_credit_type':user.co_applicant_credit_type,
        'age':user.age,
        'submission_of_application':user.submission_of_application,
        'LTV':user.ltv,
        'Region':user.region,
        'Security_Type':user.security_type,
        'dtir1':user.dtir1,
        'has_Upfront_charges':user.has_upfront_charges
    })
    prediction = int(model.predict(input)[0])
    prob = model.predict_proba(input)[0]

    return {
        'id':user.id,
        "label": "Defaulter" if prediction == 1 else "Not Defaulter",
        'prediction':prediction,
        'risk_score':float(prob[1])
    }

