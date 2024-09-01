import os
from fastapi import APIRouter, HTTPException
from app.models.db import database
import pandas as pd

router = APIRouter()

@router.post("/upload-csv/")
async def upload_csv():
    try:
        # Get the directory of the current module
        module_dir = os.path.dirname(__file__)

        # Construct the path to the CSV file relative to the module directory
        csv_file_path = os.path.join(module_dir, '..', 'corporate-purchase.csv')

        # Normalize the path (optional, but good practice)
        csv_file_path = os.path.normpath(csv_file_path)

        # Check if the file exists
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"File not found: {csv_file_path}")

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Ensure the DataFrame has the expected columns
        expected_columns = [
            'id', 'status', 'created', 'cardId', 'holderId',
            'amount', 'merchantName', 'merchantCategoryType', 'workspaceId'
        ]
        if not all(col in df.columns for col in expected_columns):
            raise HTTPException(status_code=400, detail="CSV does not have the required columns")

        # Insert data into the database
        query = """
        INSERT INTO compras_corporativas (id, status, created, cardId, holderId, amount, merchantName, merchantCategoryType, workspaceId)
        VALUES (:id, :status, :created, :cardId, :holderId, :amount, :merchantName, :merchantCategoryType, :workspaceId)
        """

        values = df.to_dict(orient='records')
        await database.execute_many(query=query, values=values)

        return {"detail": "CSV data uploaded successfully"}
    except FileNotFoundError as fnf_error:
        raise HTTPException(status_code=404, detail=str(fnf_error))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
