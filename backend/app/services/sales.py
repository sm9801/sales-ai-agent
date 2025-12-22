import pandas as pd

def add_Order_Revenue(df: pd.DataFrame) -> pd.DataFrame:
    """ Helper function to add 'Order_Revenue' column to the DataFrame.
    Adds a new column 'Order_Revenue' to the DataFrame, calculated as
    the product of 'Quantity' and 'Price'.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'Quantity' and 'Price' columns.

    Returns:
    pd.DataFrame: DataFrame with the new 'Order_Revenue' column added.
    """
    df['Order_Revenue'] = df['Quantity'] * df['Price']
    return df

def summary_metrics(df: pd.DataFrame) -> dict:
    """
    Computes summary metrics from the sales DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing sales data with 'Order_Revenue' column.

    Returns:
    dict: Dictionary containing total revenue, average order value, and total orders.
    """
    df = add_Order_Revenue(df)

    total_revenue = df['Order_Revenue'].sum()
    total_orders = len(df)
    total_units = df['Quantity'].sum()

    return {
        'total_revenue': round(total_revenue, 2),
        'total_orders': int(total_orders),
        'aov': round(float(total_revenue / total_orders), 2),
        'total_units': int(total_units),
        "avg_items_per_order": round(float(total_units / total_orders), 2),
    }

def platform_metrics(df: pd.DataFrame) :
    """
    Computes metrics grouped by sales platform.

    Parameters:
    df (pd.DataFrame): DataFrame containing sales data with 'Platform', 'Quantity',
    and 'Order_Revenue' columns (from predefined functions).

    Returns:
    dict: Dictionary containing revenue, orders, AOV, and units per order by platform.
    """
    df = add_Order_Revenue(df)

    revenue = df.groupby('Platform')['Order_Revenue'].sum()
    orders = df.groupby('Platform').size()
    units = df.groupby('Platform')['Quantity'].sum()

    aov = (revenue / orders).round(2)
    units_per_order = (units / orders).round(2)

    return {
        'revenue_by_platform': revenue.to_dict(),
        'orders_by_platform': df.groupby('Platform').size().to_dict(),
        'aov_by_platform': aov.to_dict(),
        'units_per_order_by_platform': units_per_order.to_dict(),
    }

def brand_metrics(df: pd.DataFrame) :
    """
    Computes metrics grouped by brand.

    Parameters:
    df (pd.DataFrame): DataFrame containing sales data with 'Brand', 'Quantity',
    and 'Order_Revenue' columns (from predefined functions).

    Returns:
    dict: Dictionary containing revenue, units sold, and revenue share by brand.

    """
    df = add_Order_Revenue(df)

    revenue = (
        df.groupby('Brand')['Order_Revenue']
        .sum()
        .sort_values(ascending = False)
    )

    units = (
        df.groupby('Brand')['Quantity']
        .sum()
        .sort_values(ascending = False)
    )

    revenue_share = (revenue / revenue.sum() * 100).round(2)

    return {
        'revenue_by_brand': revenue.to_dict(),
        'units_by_brand': units.to_dict(),
        'revenue_share_by_brand': revenue_share.to_dict(),
    }

def time_metrics(df: pd.DataFrame) :
    """
    Computes time-based metrics.

    Parameters:
    df (pd.DataFrame): DataFrame containing sales data with 'Order_Date' and
    'Order_Revenue' columns (from predefined functions).

    Returns:
    dict: Dictionary containing monthly revenue, month-over-month growth,
    and year-over-year growth.
    """
    df = add_Order_Revenue(df)

    monthly_revenue = (
        df.groupby('Year_Month')['Order_Revenue']
        .sum()
        .sort_index()
    )

    mom_growth = (monthly_revenue.pct_change() * 100).round(2)
    yoy_growth = (monthly_revenue.pct_change(12) * 100).round(2)

    return {
        'monthly_revenue': monthly_revenue.to_dict(),
        'mom_growth': mom_growth.to_dict(),
        'yoy_growth': yoy_growth.to_dict(),
    }

def product_metrics(df: pd.DataFrame, n: int = 10) :
    """
    Identifies the top N products by revenue and by units sold.

    Parameters:
    df (pd.DataFrame): DataFrame containing sales data with 'Product', 'Quantity',
    and 'Order_Revenue' columns (from predefined functions).

    n (int): Number of top products to return. Default is 10.
    """
    df = add_Order_Revenue(df)

    revenue = (
        df.groupby('Product')['Order_Revenue']
        .sum()
        .sort_values(ascending = False)
        .head(n)
    )

    units = (
        df.groupby('Product')['Quantity']
        .sum()
        .sort_values(ascending = False)
        .head(n)
    )

    return {
        'top_products_by_revenue': revenue.to_dict(),
        'top_products_by_units': units.to_dict()
    }



