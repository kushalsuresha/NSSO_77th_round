import pandas as pd
import numpy as np
import RegionMapping 

df = pd.read_csv('file_path')

df = df.rename(columns={
    'b11bq1': 'Serial_no',
    'b11bq3': 'Value_as_on_30_06_2018_Rs', # A
    'b11bq4': 'Value_of_Acquisition_Rs', # B
    'b11bq5': 'Value_of_Disposal_Rs', # C
    'b11bq6': 'Total_Value_Rs' # A + B - C
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