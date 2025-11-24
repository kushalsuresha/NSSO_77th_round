import pandas as pd
import numpy as np
import RegionMapping 

df_data = pd.read_csv('file_path')

print(df_data['HHID'].nunique())
print(df_data.columns)
print(len(df_data))

# Coloumn Renaming

df_data = df_data.rename(columns={
    'b3q1': 'person_number',
    'b3q3': 'Relation_to_head',
    'b3q4': 'Gender',
    'b3q5': 'Age',
    'b3q6': 'highest_educational_level_attained',
    'b3q7': 'holding_deposit_account_commercial_RRB_co_op_bank',
    'b3q8': 'holding_deposit_account_in_Post_Office',
    'b3q9': 'holding_deposit_account_in_NBFC',
    'b3q10': 'contributing_Co_op_Credit_society_SHG_JLG',
    'b3q11': 'having_deposit_in_non_inst_Agency',
    'b3q12': 'owns_any_land',
    'b3q13': 'owns_any_agricultural_land',
    'b3q14': 'holding_credit_debit_card',
    'b3q15': 'credit_debit_card_used_last_365_days',
    'b3q16': 'holding_an_e_wallet', 
    'b3q17': 'e_wallet_used_last_365_days'
    })

print(df_data.columns)

relation = {
    1: 'Self',
    2: 'Spouse',
    3: 'Married_child',
    4: 'Spouse_of_married_child',
    5: 'Unmarried_child',
    6: 'Grandchild',
    7: 'Father_Mother_or_In_Law',
    8: 'Brother_Sister_or_other_relatives',
    9: 'Servant_or_Non_relative'
    }

gender = {
    1: 'Male',
    2: 'Female',
    3: 'Transgender'
    }

education = {
    1: 'Illiterate',
    2: 'Literate_below_primary',
    3: 'Primary',
    4: 'Upper_primary',
    5: 'Secondary',
    6: 'Higher_secondary',
    7: 'Diploma_certificate_up_to_secondary',
    8: 'Diploma_certificate_higher_secondary',
    10: 'Diploma_certificate_graduation_and_above',
    11: 'Graduate',
    12: 'Postgraduate_and_above'
    }

# Decoding

df_data['Sector_Name'] = df_data['Sector'].map(RegionMapping.sector)
df_data['State_Name'] = df_data['State'].map(RegionMapping.state_encoding_map)  

df_data['District_Name'] = df_data.apply(
                                        lambda row: RegionMapping.get_district_name(
                                        row['State'], row['District']  ), axis=1 
                                        )

df_data['Relation_to_head_Name'] = df_data['Relation_to_head'].map(relation)
df_data['Gender_Name'] = df_data['Gender'].map(gender)
df_data['Education_Name'] = df_data['highest_educational_level_attained'].map(education)
df_data['Holding_bank_account'] = df_data['holding_deposit_account_commercial_RRB_co_op_bank'].map({1: 'Yes, services taken only from bank branch',
                                                                                                    2: 'Yes, services taken only from bank mitra',
                                                                                                    3: 'Yes, services taken from both bank branch and bank mitra',
                                                                                                    4: 'No account'
                                                                                                    })

df_data['Holding_deposit_account_PO'] = df_data['holding_deposit_account_in_Post_Office'].map({1: 'Yes', 2: 'No'})
df_data['Holding_deposit_account_NBFC'] = df_data['holding_deposit_account_in_NBFC'].map({1: 'Yes', 2: 'No'})
df_data['Contributing_Co_op_Credit_society_SHG_JLG'] = df_data['contributing_Co_op_Credit_society_SHG_JLG'].map({1: 'Yes', 2: 'No'})
df_data['Having_deposit_in_non_inst_Agency'] = df_data['having_deposit_in_non_inst_Agency'].map({1: 'Yes', 2: 'No'})
df_data['Owns_any_land'] = df_data['owns_any_land'].map({1: 'Yes', 2: 'No'})
df_data['Owns_any_agricultural_land'] = df_data['owns_any_agricultural_land'].map({1: 'Yes', 2: 'No'})
df_data['Holding_credit_debit_card'] = df_data['holding_credit_debit_card'].map({1: 'Yes', 2: 'No'})
df_data['Credit_debit_card_used_last_365_days'] = df_data['credit_debit_card_used_last_365_days'].map({1: 'Yes', 2: 'No'})
df_data['Holding_an_e_wallet'] = df_data['holding_an_e_wallet'].map({1: 'Yes', 2: 'No'})
df_data['E_wallet_used_last_365_days'] = df_data['e_wallet_used_last_365_days'].map({1: 'Yes', 2: 'No'})

df_data['person_id'] = df_data['HHID'].astype(str) + '_' + df_data['person_number'].astype(str)

df_data.to_csv('file_path', index=False)
