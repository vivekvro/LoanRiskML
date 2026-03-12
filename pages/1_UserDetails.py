import streamlit as st
import requests
import os,dotenv
dotenv.load_dotenv()
from pandas import DataFrame

MAIN_URL = os.getenv("MAIN_URL")


insert_url = MAIN_URL+"/insertrecord"
select = st.selectbox(
    "Select :",
    ("Search Records", "Insert Records"),
)

# INSERT PAGE
if select == "Insert Records":

    st.header("Insert Loan Record")

    with st.form("loan_form"):

        id = st.number_input("User ID", min_value=1)
        year = st.number_input("Year", min_value=2001)

        gender = st.selectbox("Gender", ['Sex Not Available','Male','Joint','Female'])
        loan_limit = st.selectbox("Loan Limit", ['cf','ncf'])
        approv_in_adv = st.selectbox("Approval in Advance", ['nopre','pre'])
        loan_type = st.selectbox("Loan Type", ['type1','type2','type3'])
        loan_purpose = st.selectbox("Loan Purpose", ['p1','p4','p3','p2'])

        credit_worthiness = st.selectbox("Credit Worthiness", ['l1','l2'])
        open_credit = st.selectbox("Open Credit", ['nopc','opc'])
        business_or_commercial = st.selectbox("Business / Commercial", ['nob/c','b/c'])

        neg_ammortization = st.selectbox("Negative Amortization", ['not_neg','neg_amm'])
        interest_only = st.selectbox("Interest Only", ['not_int','int_only'])
        lump_sum_payment = st.selectbox("Lump Sum Payment", ['not_lpsm','lpsm'])

        construction_type = st.selectbox("Construction Type", ['sb','mh'])
        occupancy_type = st.selectbox("Occupancy Type", ['pr','sr','ir'])

        secured_by = st.selectbox("Secured By", ['home','land'])
        total_units = st.selectbox("Total Units", ['1U','2U','3U','4U'])

        credit_type = st.selectbox("Credit Type", ['EXP','EQUI','CRIF','CIB'])
        co_applicant_credit_type = st.selectbox("Co-applicant Credit Type", ['CIB','EXP'])

        age = st.selectbox("Age Group", ['25-34','55-64','35-44','45-54','65-74','>74','<25'])

        submission_of_application = st.selectbox("Submission of Application", ['to_inst','not_inst'])

        region = st.selectbox("Region", ['south','North','central','North-East'])
        security_type = st.selectbox("Security Type", ['direct','Indriect'])

        loan_amount = st.number_input("Loan Amount", min_value=0.0)
        rate_of_interest = st.number_input("Rate of Interest", min_value=0.0)
        interest_rate_spread = st.number_input("Interest Rate Spread")
        upfront_charges = st.number_input("Upfront Charges", min_value=0.0)

        term = st.number_input("Loan Term (months)", min_value=96, max_value=360)

        property_value = st.number_input("Property Value", min_value=0.0)
        income = st.number_input("Income", min_value=0.0)

        credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
        ltv = st.number_input("LTV")
        dtir1 = st.number_input("DTI Ratio")

        submit = st.form_submit_button("Submit Record")

    if submit:
        with st.spinner("inserting....."):
            data={
                    "id": id,
                    "year": year,
                    "gender": gender,
                    "loan_limit": loan_limit,
                    "approv_in_adv": approv_in_adv,
                    "loan_type": loan_type,
                    "loan_purpose": loan_purpose,
                    "credit_worthiness": credit_worthiness,
                    "open_credit": open_credit,
                    "business_or_commercial": business_or_commercial,
                    "neg_ammortization": neg_ammortization,
                    "interest_only": interest_only,
                    "lump_sum_payment": lump_sum_payment,
                    "construction_type": construction_type,
                    "occupancy_type": occupancy_type,
                    "secured_by": secured_by,
                    "total_units": total_units,
                    "credit_type": credit_type,
                    "co_applicant_credit_type": co_applicant_credit_type,
                    "age": age,
                    "submission_of_application": submission_of_application,
                    "region": region,
                    "security_type": security_type,
                    "loan_amount": loan_amount,
                    "rate_of_interest": rate_of_interest,
                    "interest_rate_spread": interest_rate_spread,
                    "upfront_charges": upfront_charges,
                    "term": term,
                    "property_value": property_value,
                    "income": income,
                    "credit_score": credit_score,
                    "ltv": ltv,
                    "dtir1": dtir1
                    }
            response = requests.post(url=insert_url,json=data)
            st.write(response.json())


# SEARCH PAGE
elif select == "Search Records":
    st.header("Search Record")
    select_type = st.selectbox("select",['User Record','Loan Risk by User'])
    user_id = st.number_input("Enter User ID", min_value=1)

    if st.button("Search"):
        with st.spinner("fetching...."):
            if select_type=='User Record':
                url = f"{MAIN_URL}/getUserrecord/{user_id}"
            elif select_type=="Loan Risk by User":
                url = f"{MAIN_URL}/getLoanriskrecord/{user_id}"

            response = requests.get(url=url)
            st.dataframe(DataFrame([response.json()]))
