# NSSO_77th_round
Python scripts to label variables of the National Sample Survey Office (NSSO) 77th Round block files.

Released in September 2021, the 77th round of the National Sample Survey (NSS)—conducted by the National Statistical Office (NSO) between January and December 2019—focused on two main integrated subjects:

1. Schedule 33.1: Land and Livestock Holdings of Households and Situation Assessment of Agricultural Households.
2. Schedule 18.2: Debt and Investment data of the Households

## NSSO Data Structure

* Blocks 1-4 (Identification and Characteristics): cover the essential information for household identification, basic demographic characteristics, and survey particulars.

* Blocks 5-10 (Land and Livestock / Situation Assessment of Agricultural Households): This is the core thematic area, focusing on the economic welfare and production assets of households engaged in agriculture. It collects detailed data on:
  * Land possessed and operated.
  * Ownership and maintenance of livestock.
  * The overall economic situation, income sources, consumption patterns, and expenditure of agricultural households.

* Blocks 11 onwards (Debt and Investment Focus): This thematic block is dedicated to capturing the financial position of all surveyed households, regardless of their primary occupation. It collects comprehensive data on:
  * The level and sources of outstanding debt/liabilities.
  * Assets held by the household (including financial and physical assets).
  * Capital expenditure and transactions related to fixed assets and land.

## Structure of the repository

The scripts in this repository assign descriptive labels to source variables and create a separate, labeled copy for variables requiring value mapping, enhancing readability for further analysis. The scripts in the [Codes](https://github.com/kushalsuresha/NSSO_77th_round/tree/main/Codes) folder are as follows:

* [RegionMapping.py](https://github.com/kushalsuresha/NSSO_77th_round/blob/main/Codes/RegionMapping.py): Core utility script leveraged for region mapping (states and districts), across other labeling files.
* bX.py: A set of scripts with the numerical suffix (like b3, b4, b11) corresponds to specific blocks of NSSO 77th data blocks.
