from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/filter")
def filter_csv(column: str, value: str):
    file_path = "C:/data/dataset.csv"  # Make sure this file exists
    try:
        df = pd.read_csv(file_path)
        if column not in df.columns:
            return {"error": f"Column '{column}' not found in CSV"}
        filtered_df = df[df[column] == value]
        return filtered_df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}


