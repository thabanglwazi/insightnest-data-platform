# price_cleaner.py

import pandas as pd

def clean_veg_price_data(df):
    def assign_season(month):
        if month in [12, 1, 2]:
            return str('Summer')
        elif month in [3, 4, 5]:
            return str('Winter')
        elif month in [6, 7, 8]:
            return str('Monsoon')
        else:
            return str('Autumn')

    df = df.copy()

    # Convert 'Price Dates' to datetime
    df['Price Dates'] = pd.to_datetime(df['Price Dates'], format="%d-%m-%Y", errors='coerce')

    # Convert all price columns to float with 2 decimals
    for col in df.columns:
        if col != 'Price Dates':
            df[col] = pd.to_numeric(df[col], errors='coerce').round(2)

    # Add Month and Season columns
    df['Month'] = df['Price Dates'].dt.month
    df['Season'] = df['Month'].apply(assign_season)

    return df
