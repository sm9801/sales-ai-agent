import pandas as pd

# calculate summary KPIs from sales data
def calculate_summary_kpis(df: pd.DataFrame) -> dict:
    kpis = {}

    # Basic sanity
    kpis["num_rows"] = len(df)

    # Revenue
    if "revenue" in df.columns:
        kpis["total_revenue"] = float(df["revenue"].sum())
    else:
        kpis["total_revenue"] = None

    # Units
    if "units" in df.columns:
        kpis["total_units"] = int(df["units"].sum())
    else:
        kpis["total_units"] = None

    # Dimensions
    kpis["num_products"] = df["product"].nunique() if "product" in df.columns else None
    kpis["num_countries"] = df["country"].nunique() if "country" in df.columns else None

    return kpis

