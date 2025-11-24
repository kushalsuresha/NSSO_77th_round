import pandas as pd
import numpy as np
import RegionMapping 

df_data = pd.read_csv('file_path')

print(df_data['HHID'].nunique())
print(df_data.columns)
print(len(df_data))

print(df_data['State'].unique())

df_data = df_data.rename(columns={
    'b4q1': 'Household_size',
    'b4q2': 'Religion',
    'b4q3': 'Social_Group',
    'b4q4': 'Household_type',
    'b4q5': 'acres_homestead_land_possessed',
    'b4q6dot1': 'acres_owned_possed',
    'b4q6dot2': 'acres_leased_in',
    'b4q6dot3': 'acres_otherwise_possessed',
    'b4q6dot4': 'acres_leased_out',
    'b4q7': 'operated_land_for_agricultural_activities_last_365_days',
    'b4q8dot1': 'acres_operated_by_household',
    'b4q8dot2': 'acres_operated_under_kitchen_garden',
    'b4q9dot1': 'PMJJBY',
    'b4q9dot2': 'PMSBY',
    'b4q9dot3': 'APY'
})
print(df_data.head())

religion = {
    1: 'Hinduism',
    2: 'Islam',
    3: 'Christianity',
    4: 'Sikhism',
    5: 'Jainism',
    6: 'Buddhism',
    7: 'Zoroastrianism',
    8: 'Others'
}

social_group = {
    1: 'ST',
    2: 'SC',
    3: 'OBC',
    9: 'General'
}

household_type = {
    1: {
        1: 'self_employed_agriculture',
        2: 'self_employed_non_agriculture',
        3: 'regular_wage',
        4: 'casual_labour_agriculture',
        5: 'casual_labour_non_agriculture',
        9: 'other'
    },
    2: {
        1: 'self_employed',
        2: 'regular_wage',
        3: 'casual_labour',
        9: 'other'
    } 
}

def get_h_type_name(sector_code: int, type_code: int, mapping_data: dict = household_type) -> str:

    if sector_code not in mapping_data:
        return f"Error: Sector code '{sector_code}' not found in list."
    
    sector = mapping_data[sector_code]
    
    if type_code not in sector:
        return f"Error: H_type code '{type_code}' not found for Sector code '{sector_code}'."

    return sector[type_code]

# Decoding


df_data['Sector_Name'] = df_data['Sector'].map(RegionMapping.sector)
df_data['State_Name'] = df_data['State'].map(RegionMapping.state_encoding_map)  

df_data['District_Name'] = df_data.apply(
                                        lambda row: RegionMapping.get_district_name(
                                        row['State'], row['District']  ), axis=1 
                                        )

df_data['Social_Group_Name'] = df_data['Social_Group'].map(social_group)

df_data['household_type_name'] = df_data.apply(
                                            lambda row: get_h_type_name(
                                            row['Sector'], row['Household_type']), axis=1 
                                            )

df_data['operated_land_for_agricultural_name'] = df_data['operated_land_for_agricultural_activities_last_365_days'].map({1: 'Yes', 2: 'No'})

df_data.to_csv('file_path', index=False)  