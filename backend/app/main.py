from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi import UploadFile, File, HTTPException
from app.utils.loader import load_sales_file
from app.services.data_store import set_sales_data
from app.services.data_store import get_sales_data
from app.services.sales import calculate_summary_kpis

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
    return {"status": "ok"}

@app.post("/upload")
async def upload_sales_file(file: UploadFile = File(...)):
    try:
        df = load_sales_file(file)

        set_sales_data(df)

        return {
            "message": "File uploaded successfully",
            "rows": df.shape[0],
            "columns": df.shape[1],
            "column_names": df.columns.tolist(),
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/metrics/summary")
def get_summary_kpis():
    try :
        df = get_sales_data()
        kpis = calculate_summary_kpis(df)
        return kpis
    
    except Exception as e :
        raise HTTPException(status_code = 400, detail = str(e))

@app.get("/ping")
def ping():
    return {"message": "FastAPI is connected!"}