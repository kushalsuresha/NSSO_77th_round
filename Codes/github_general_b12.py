import pandas as pd
import numpy as np
import RegionMapping 

df = pd.read_csv('file_path')

df = df.rename(columns={
    
    'b12q1': 'Loan_Serial_no',
    'b12q2': 'Year_of_borrowing',
    'b12q3': 'Loan_unpaid_as_on_30_06_2018',
    'b12q4': 'Amount_borrowed_originally_Rs',
    'b12q5': 'Credit_agency',
    'b12q6': 'Scheme_of_lending',
    'b12q7': 'Tenure_of_loan',
    'b12q8': 'Nature_of_interest',
    'b12q9': 'Annual_rate_of_interest_perc',
    'b12q10': 'Purpose_of_loan',
    'b12q11': 'Loan_is_secured',
    'b12q12': 'Amount_repaid_01_07_2018_to_survey_date_Rs',
    'b12q13': 'Amount_written_off_01_07_2018_to_survey_date_Rs',
    'b12q14': 'Amount_outstanding_as_on_date_of_survey_Rs',
    'b12q15': 'Amount_outstanding_as_on_30_06_2018_Rs'
    })

print(df.head())

credit_agency_encoding = {
    1: 'Scheduled_commercial_bank',
    2: 'Regional_rural_bank',
    3: 'Co-operative_society',
    4: 'Co-operative_bank',
    5: 'Insurance_companies',
    6: 'Provident_fund',
    7: 'Employer',
    8: 'Financial_corporation',
    9: 'Other', 
    10: 'NBFCs_and_micro',
    11: 'Bank_linked_SHG_JLG',
    12: 'Non-bank_linked_SHG_JLG',
    13: 'Other_institutional_agencies', 
    14: 'Landlord',
    15: 'Agricultural_moneylender',
    16: 'Professional_moneylender',
    17: 'Input_supplier',
    18: 'Relatives_and_friends',
    19: 'Chit_fund',
    20: 'Market_commission_agent_traders',
    }

scheme_of_lending_encoding = {
    1: 'Mudra',
    2: 'Stand_Up_India_scheme',
    3: 'NRLM_NULM',
    4: 'Other_central_govt_schemes',
    5: 'Exclusive_State_scheme',
    6: 'Exclusive_bank_scheme',
    7: 'Kisan_Credit_Card',
    8: 'Crop_loan_other_agricultural_loan',
    9: 'Not_covered_under_any_scheme'
}

loan_tenure_encoding = {
    1: 'Short-term_(less_than_1_year)',
    2: 'Medium-term_(1_to_3_years)',
    3: 'Long-term_(3_years_or_more)'
}

nature_of_interest_encoding = {
    1: 'Interest-free',
    2: 'Simple_interest',
    3: 'Compound_interest'
}

purpose_of_loan_encoding = {
    # Farm Business Expenditure
    1: 'Capital_expenditure_in_farm_business',
    2: 'Revenue_expenditure_in_farm_business',
    3: 'Capital_expenditure_in_non-farm_business',
    4: 'Revenue_expenditure_in_non-farm_business',
    5: 'Expenditure_on_litigation',
    6: 'Repayment_of_debt',
    7: 'Financial_investment_expenditure',
    8: 'Expenditure_on_education',
    9: 'Other_purpose', 
    10: 'Expenditure_on_medical_treatment',
    11: 'Expenditure_on_housing',
    12: 'Other_household_expenditure'
}

# Labeling


df['Sector_Name'] = df['Sector'].map(RegionMapping.sector)
df['State_Name'] = df['State'].map(RegionMapping.state_encoding_map)  

df['District_Name'] = df.apply(
                                lambda row: RegionMapping.get_district_name(
                                row['State'], row['District']  ), axis=1 
                                )

df['Loan_unpaid_as_on_30_06_2018_Name'] = df['Loan_unpaid_as_on_30_06_2018'].map({1: 'Yes', 2: 'No'})
df['Credit_agency_Name'] = df['Credit_agency'].map(credit_agency_encoding)
df['Scheme_of_lending_Name'] = df['Scheme_of_lending'].map(scheme_of_lending_encoding)
df['Tenure_of_loan_Name'] = df['Tenure_of_loan'].map(loan_tenure_encoding)
df['Nature_of_interest_Name'] = df['Nature_of_interest'].map(nature_of_interest_encoding)
df['Purpose_of_loan_Name'] = df['Purpose_of_loan'].map(purpose_of_loan_encoding)
df['Loan_is_secured_Name'] = df['Loan_is_secured'].map({1: 'Yes', 2: 'No'})

df.to_csv('file_path', index=False)  
