import pandas as pd
import numpy as np
import RegionMapping 

df = pd.read_csv('file_path')

df = df.rename(columns={
    'b11aq1': 'Asset_serial_no',
    'b11aq3': 'Value_as_on_30_06_2018_Rs',# A
    'b11aq4': 'Value_of_Acquisition_Rs', # B
    'b11aq5': 'Value_of_Disposal_Rs', # C
    'b11aq6': 'Total_Value_Rs' # A + B - C
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