import pandas as pd


def load_performance_csvfile(filepath, encoding='utf-8'):
    df = pd.read_csv(filepath, encoding=encoding)
    df.date = pd.to_datetime(df.date, format='%Y%m%d')
    df.asset_value = df.asset_value.str.replace(' |,', '').astype(float)
    df.asset_shares = df.asset_shares.str.replace(' |,', '').astype(int)
    df.asset_value_change = df.asset_value_change.str.replace(' |,', '').astype(float)
    df = df.drop(columns=['blank_column'])
    return df



