import pandas as pd
import numpy as np
import RegionMapping 

df = pd.read_csv('file_path')

df = df.rename(columns={
    'b13q1': 'Kind_Loan_Serial_no',
    'b13q2': 'Period_of_kind_loan',
    'b13q3': 'Source_of_kind_loan',
    'b13q4': 'Purpose_of_kind_loan',
    'b13q5': 'Amount_outstanding_as_on_date_of_survey_(Rs)'
    })

print(df.head())

kind_loan_period_encoding = {
    1: 'Less_than_1_month',
    2: '1_month_and_above_but_less_than_3_months',
    3: '3_month_and_above_but_less_than_6_months',
    4: '6_month_and_above_but_less_than_1_year',
    5: 'One_year_and_above'
}

kind_loan_source_encoding = {
    1: 'Input_supplier',
    2: 'Relatives_and_friends',
    3: 'Doctors_lawyers_&_other_professionals', 
    9: 'Other' 
}

kind_loan_purpose_encoding = {
    1: 'Revenue_expenditure_in_farm_business',
    2: 'Revenue_expenditure_in_non_farm_business',
    3: 'Household_expenditure',
    9: 'Other_expenditure'
}

# Labeling


df['Sector_Name'] = df['Sector'].map(RegionMapping.sector)
df['State_Name'] = df['State'].map(RegionMapping.state_encoding_map)  

df['District_Name'] = df.apply(
                                lambda row: RegionMapping.get_district_name(
                                row['State'], row['District']  ), axis=1 
                                )

df['Period_of_kind_loan_Name'] = df['Period_of_kind_loan'].map(kind_loan_period_encoding)
df['Source_of_kind_loan_Name'] = df['Source_of_kind_loan'].map(kind_loan_source_encoding)
df['Purpose_of_kind_loan_Name'] = df['Purpose_of_kind_loan'].map(kind_loan_purpose_encoding)

df.to_csv('file_path', index=False)  