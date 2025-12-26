"""Metrics API routes for the application."""

from app.services.sales import (brand_metrics, platform_metrics,
                                product_metrics, summary_metrics, time_metrics)
from app.utils.data_store import get_sales_data
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/summary")
def get_summary_metrics():
    try:
        df = get_sales_data()
        return summary_metrics(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/time")
def get_time_metrics():
    try:
        df = get_sales_data()
        return time_metrics(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/platform")
def get_platform_metrics():
    try:
        df = get_sales_data()
        return platform_metrics(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/brand")
def get_brand_metrics():
    try:
        df = get_sales_data()
        return brand_metrics(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    
@router.get("/products")
def get_product_metrics():
    try:
        df = get_sales_data()
        return product_metrics(df)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e)) from e
