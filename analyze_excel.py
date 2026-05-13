import pandas as pd
import os

# Test with one experience file
file_path = r"db\exp\2020-2021\Accenture\ECE_2020-21_Recruitment Process Experience.xlsx"

print(f"Analyzing file: {file_path}")

try:
    # Load the Excel file
    excel_file = pd.ExcelFile(file_path)

    print(f"Number of sheets: {len(excel_file.sheet_names)}")
    print(f"Sheet names: {excel_file.sheet_names}")

    # Read each sheet and display basic info
    for sheet_name in excel_file.sheet_names:
        print(f"\nSheet: {sheet_name}")
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Shape: {df.shape}")
        print("Columns:", df.columns.tolist())
        print("First 3 rows:")
        print(df.head(3))
        print("-" * 50)

except Exception as e:
    print(f"Error reading file: {e}")