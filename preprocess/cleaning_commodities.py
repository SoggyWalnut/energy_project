import numpy as np
import pandas as pd 

np.set_printoptions(linewidth=100000)

# Read data from original data file
df = pd.read_csv("../input/all_energy_statistics.csv")

# Preprocess column commodity_transaction
def preprocess_commodities(df):
    # Split data in commodity_transaction column    into three columns for easier data processing 
    split_commodities = df['commodity_transaction'].str.split(" - | – ",  expand=True)
    split_commodities.columns = ["commodity","transaction_type","additional_transaction_info"]
    
    # Lower all string from commodity column
    split_commodities['commodity'] = split_commodities['commodity'].str.lower()

    # Lower and remove trailing whitespaces from all string from transaction_type column
    split_commodities['transaction_type'] = split_commodities['transaction_type'].str.lower().str.strip()
    # Fix punctuation errors in transaction_type column
    split_commodities['transaction_type'] = split_commodities['transaction_type'].str.replace("transformatin", "transformation")
    split_commodities['transaction_type'] = split_commodities['transaction_type'].str.replace("non energy uses", "consumption for non-energy uses")
    split_commodities['transaction_type'] = split_commodities['transaction_type'].str.replace(" /", "/")
    split_commodities['transaction_type'] = split_commodities['transaction_type'].str.replace("/ ", "/")

    # Lower all string from additional_transaction_info column
    split_commodities['additional_transaction_info'] = split_commodities['additional_transaction_info'].str.lower()

    # Drop old column and add new columns
    df = df.drop('commodity_transaction', axis = 1)
    # Column commodity is not added due to duplication with transaction_type column
    df = pd.concat([df, split_commodities['transaction_type'], split_commodities['additional_transaction_info']], axis=1)
    return df

# Process column unit
def preprocess_unit(df):
    # Split data in unit column into tưo columns for easier data processing 
    split_unit = df['unit'].str.split(",",  expand=True)
    split_unit.columns = ["metrics", "calculation_unit"]
    
    # Lower and remove trailing whitespaces from string in calculation_unit column
    split_unit['calculation_unit'] = split_unit['calculation_unit'].str.lower().str.strip()

    # Lower string in metrics column
    split_unit['metrics'] = split_unit['metrics'].str.lower()

    # Drop old column and add new columns
    df = df.drop('unit', axis = 1)
    df = pd.concat([df, split_unit['metrics'], split_unit['calculation_unit']], axis=1)
    return df

preprocessed_commodity_df = preprocess_commodities(df)
preprocessed_unit_df = preprocess_unit(preprocessed_commodity_df)
preprocessed_unit_df.to_csv('../output/cleaned_energy_data.csv',encoding='utf-8', index=False, lineterminator='\n')