import pandas as pd

def filter_smaller_value(df: pd.DataFrame, threshold = 20) -> pd.DataFrame:
    """This function filter the rows that have value less than the given value
    """
    filtered_df = df.loc[df['value'] > threshold]
    return filtered_df