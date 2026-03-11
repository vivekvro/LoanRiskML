import streamlit as st

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
        st.success("Record submitted")

# SEARCH PAGE
elif select == "Search Records":

    st.header("Search Record")

    user_id = st.number_input("Enter User ID", min_value=1)

    if st.button("Search"):
        st.write("Fetching record...")