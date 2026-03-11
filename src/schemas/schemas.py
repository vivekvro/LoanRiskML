from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from pandas import DataFrame

class UserRecord(BaseModel):

    id: Annotated[int, Field(gt=0, description="Unique identifier for the loan application/user", examples=[12308,34521])]
    year: Annotated[int, Field(gt=2000, description="Year the loan was issued (YYYY format)", examples=[2025,2026])]

    gender: Annotated[Literal['Sex Not Available','Male','Joint','Female'],
                      Field(description="Gender of applicant (Male, Female, Joint, or unavailable)")]

    loan_limit: Annotated[Literal['cf','ncf'],
                          Field(description="Loan limit category (cf = conforming loan, ncf = non-conforming loan)")]

    approv_in_adv: Annotated[Literal['nopre','pre'],
                             Field(description="Whether the loan was pre-approved before formal application (pre = pre-approved)")]

    loan_type: Annotated[Literal['type1','type2','type3'],
                         Field(description="Category/type of loan product offered by lender")]

    loan_purpose: Annotated[Literal['p1','p4','p3','p2'],
                            Field(description="Purpose of the loan such as purchase, refinance, etc.")]

    credit_worthiness: Annotated[Literal['l1','l2'],
                                 Field(description="Borrower's creditworthiness category (l1 = higher quality borrower, l2 = lower quality)")]

    open_credit: Annotated[Literal['nopc','opc'],
                           Field(description="Whether borrower currently has open credit lines (opc = open credit present)")]

    business_or_commercial: Annotated[Literal['nob/c','b/c'],
                                      Field(description="Indicates if loan is for business/commercial purposes (b/c = business/commercial)")]

    neg_ammortization: Annotated[Literal['not_neg','neg_amm'],
                                 Field(description="Indicates whether loan allows negative amortization (loan balance may increase)")]

    interest_only: Annotated[Literal['not_int','int_only'],
                             Field(description="Whether the loan allows interest-only payments during an initial period")]

    lump_sum_payment: Annotated[Literal['not_lpsm','lpsm'],
                                Field(description="Indicates if borrower can make a lump-sum payment option")]

    construction_type: Annotated[Literal['sb','mh'],
                                 Field(description="Property construction type (sb = site-built home, mh = manufactured home)")]

    occupancy_type: Annotated[Literal['pr','sr','ir'],
                              Field(description="Occupancy status of the property (pr = primary residence, sr = secondary residence, ir = investment property)")]

    secured_by: Annotated[Literal['home','land'],
                          Field(description="Type of asset used as collateral for the loan")]

    total_units: Annotated[Literal['1U','2U','3U','4U'],
                           Field(description="Number of housing units in the property")]

    credit_type: Annotated[Literal['EXP','EQUI','CRIF','CIB'],
                           Field(description="Credit bureau used to obtain borrower's credit report (Experian, Equifax, etc.)")]

    co_applicant_credit_type: Annotated[Literal['CIB','EXP'],
                                        Field(description="Credit bureau used for the co-applicant's credit report")]

    age: Annotated[Literal['25-34','55-64','35-44','45-54','65-74','>74','<25'],
                   Field(description="Age range category of the borrower")]

    submission_of_application: Annotated[Literal['to_inst','not_inst'],
                                         Field(description="Whether the loan application was submitted through an institution")]

    region: Annotated[Literal['south','North','central','North-East'],
                      Field(description="Geographical region where the borrower resides")]

    security_type: Annotated[Literal['direct','Indriect'],
                             Field(description="Type of security used in the loan agreement (direct or indirect)")]

    loan_amount: Annotated[float, Field(gt=0, le=4000000,
                        description="Total loan amount requested by borrower",
                        examples=[250000, 450000])]

    rate_of_interest: Annotated[float, Field(ge=0, le=10,
                        description="Annual interest rate applied to the loan",
                        examples=[3.8, 4.2])]

    interest_rate_spread: Annotated[float, Field(ge=-5, le=5,
                        description="Difference between loan interest rate and benchmark rate",
                        examples=[0.3, 0.8])]

    upfront_charges: Annotated[float, Field(ge=0, le=70000,
                        description="Initial fees charged by lender at loan origination",
                        examples=[1200, 3500])]

    term: Annotated[int, Field(ge=96, le=360,
                    description="Loan duration in months",
                    examples=[180, 360])]

    property_value: Annotated[float, Field(gt=0, le=20000000,
                        description="Estimated market value of the property used as collateral",
                        examples=[350000, 800000])]

    income: Annotated[float, Field(ge=0, le=600000,
                description="Borrower's income used for loan eligibility assessment",
                examples=[4500, 12000])]

    credit_score: Annotated[int, Field(ge=300, le=900,
                        description="Borrower's credit score indicating credit risk",
                        examples=[650, 780])]

    ltv: Annotated[float, Field(gt=0, le=8000,
                description="Loan-to-Value ratio (loan amount divided by property value)",
                examples=[65.4, 80.2])]

    dtir1: Annotated[float, Field(ge=0, le=70,
                description="Debt-to-Income ratio representing borrower's monthly debt obligations relative to income",
                examples=[32, 45])]

    @computed_field
    @property
    def has_upfront_charges(self) -> int:
        return int(self.upfront_charges > 0)