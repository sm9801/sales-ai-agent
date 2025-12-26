import pandas as pd

sales_df: pd.DataFrame | None = None

def set_sales_data(df: pd.DataFrame):
    global sales_df
    sales_df = df

def get_sales_data() -> pd.DataFrame:
    if sales_df is None:
        raise ValueError("No sales data uploaded yet")
    return sales_df
