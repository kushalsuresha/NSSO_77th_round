import pandas as pd
import numpy as np
import RegionMapping 

df = pd.read_csv('file_path')
# df = pd.read_stata('file_path') # For .dta files

df = df.rename(columns={
    # UMCE: Usual Monthly Consumer Expenditure
    'b4q10dot1': 'UMCE_out_of_purchase_A',
    'b4q10dot2': 'UMCE_from_home_grown_stock_B',
    'b4q10dot3': 'UMCE_from_wages_in_kind_gifts_etc_C',
    'b4q10dot4': 'Expenditure_on_household_durable_last_365_days_D',
    'b4q10dot5': 'UMCE_total'  # [A+B+C+(D/12)] 
    })
print(df.head())


# Decoding


df['Sector_Name'] = df['Sector'].map(RegionMapping.sector)
df['State_Name'] = df['State'].map(RegionMapping.state_encoding_map)  

df['District_Name'] = df.apply(
                                        lambda row: RegionMapping.get_district_name(
                                        row['State'], row['District']  ), axis=1 
                                        )


df.to_csv('file_path', index=False)  
