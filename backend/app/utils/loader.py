import pandas as pd

def load_sales_file(file):
    filename = file.filename.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        df = pd.read_excel(file.file)
    else:
        raise ValueError("Unsupported file type")

    return df
