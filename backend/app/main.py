"""
Main FastAPI application for sales data metrics.
"""
from app.services.sales import (brand_metrics, platform_metrics,
                                product_metrics, summary_metrics, time_metrics)
from app.utils.data_store import get_sales_data, set_sales_data
from app.utils.loader import load_sales_file
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

# run backend: python -m uvicorn app.main:app --reload
# run frontend: npm run dev

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/upload")
async def upload_sales_file(file: UploadFile = File(...)):
    """ Docstring for upload_sales_file

    Uploads a sales data file and stores its content.
    :param file: Sales data file containing information on brand, platform, product, etc.
    :type file: CSV or Excel file
    :return: upload status, rows, and columns
    """
    try:
        df = load_sales_file(file)

        set_sales_data(df)

        return {
            "message": "File uploaded successfully",
            "rows": df.shape[0],
            "columns": df.columns.tolist(),
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

# @app.get("/metrics/summary")
# def get_summary_kpis():
#     try :
#         df = get_sales_data()
#         kpis = calculate_summary_kpis(df)
#         return kpis
#     except Exception as e :
#         raise HTTPException(status_code = 400, detail = str(e))
# from app.services.sales import (brand_metrics, platform_metrics,
#                                 product_metrics, summary_metrics, time_metrics)


@app.get("/metrics/summary")
def get_summary_metrics():
    """retrieve summary sales metrics."""
    try :
        df = get_sales_data()
    except ValueError :
        return {
            "total_revenue": 0,
            "total_orders": 0,
            "aov": 0,
            "total_units": 0,
            "avg_items_per_order": 0,
        }
    return summary_metrics(df)


@app.get("/metrics/platform")
def get_platform_metrics():
    """retrieve platform sales metrics."""
    df = get_sales_data()

    if df is None:
        return {"error": "No data uploaded yet"}
    return platform_metrics(df)


@app.get("/metrics/products")
def get_product_metrics():
    """retrieve product sales metrics."""
    df = get_sales_data()

    if df is None:
        return {"error": "No data uploaded yet"}
    return product_metrics(df)

@app.get("/metrics/brands")
def get_brand_metrics() :
    """retrieve brand sales metrics."""
    df = get_sales_data()

    if df is None :
        return{"error": "No data uploaded yet"}
    return brand_metrics(df)

@app.get("/metrics/time")
def get_time_metrics() :
    """retrieve time sales metrics (MoM, YoY Growth)."""
    df = get_sales_data()

    if df is None :
        return{"error": "No data uploaded yet"}
    return time_metrics(df)


@app.get("/ping")
def ping():
    """Ping endpoint to test connectivity."""
    return {"message": "FastAPI is connected!"}
