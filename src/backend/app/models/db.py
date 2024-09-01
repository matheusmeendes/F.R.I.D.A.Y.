import pandas as pd

# Load the CSV file into a pandas DataFrame
csv_file_path = '../../corporate_purchase.csv'
df = pd.read_csv(csv_file_path)

def execute_query(sql_query: str):
    # Execute the SQL query on the DataFrame
    result = df.query(sql_query)
    return result.to_dict(orient="records")
