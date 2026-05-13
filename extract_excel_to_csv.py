import pandas as pd
import os
import glob
import sys
from pathlib import Path

def sanitize_filename(filename):
    """Create a safe filename by removing invalid characters"""
    # Remove invalid characters for Windows filenames
    safe_filename = "".join(c for c in filename if c.isalnum() or c in (' ','-','_','.')).rstrip()
    # Replace spaces with underscores
    safe_filename = safe_filename.replace(' ', '_')
    # Handle empty filenames
    if not safe_filename:
        safe_filename = "unnamed_sheet"
    return safe_filename

def convert_excel_to_csv(input_path, output_dir):
    """Convert Excel file to CSV files, one per sheet"""
    try:
        print(f"Processing: {input_path}")

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Load Excel file
        excel_file = pd.ExcelFile(input_path)

        print(f"  Found {len(excel_file.sheet_names)} sheets")

        # Process each sheet
        for sheet_name in excel_file.sheet_names:
            try:
                df = pd.read_excel(input_path, sheet_name=sheet_name)

                # Skip empty sheets
                if df.empty:
                    print(f"  Skipping empty sheet: {sheet_name}")
                    continue

                # Clean column names
                new_columns = []
                for col in df.columns:
                    if 'Unnamed:' in str(col):
                        # Replace with a generic name
                        new_columns.append(f"Column_{col.split(':')[1].strip()}" if ':' in str(col) else "Unnamed_Column")
                    else:
                        new_columns.append(col)
                df.columns = new_columns

                # Remove entirely empty columns
                df = df.dropna(axis=1, how='all')

                # Remove entirely empty rows
                df = df.dropna(axis=0, how='all')

                # Skip if dataframe is empty after cleaning
                if df.empty:
                    print(f"  Skipping empty sheet after cleaning: {sheet_name}")
                    continue

                # Create safe filename for sheet
                safe_sheet_name = sanitize_filename(sheet_name)

                # Ensure filename is not too long
                if len(safe_sheet_name) > 100:
                    safe_sheet_name = safe_sheet_name[:100]

                # Save as CSV
                csv_path = os.path.join(output_dir, f"{safe_sheet_name}.csv")
                df.to_csv(csv_path, index=False)
                print(f"  Saved: {csv_path}")

            except Exception as sheet_error:
                print(f"  Error processing sheet '{sheet_name}': {sheet_error}")
                continue

    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

    return True

def process_all_excel_files():
    """Process all Excel files in db/exp and db/que"""
    print("Starting Excel to CSV conversion process...")

    # Count total files to process
    exp_files = glob.glob("db/exp/**/*.xlsx", recursive=True)
    que_files = glob.glob("db/que/**/*.xlsx", recursive=True)
    total_files = len(exp_files) + len(que_files)

    print(f"Found {len(exp_files)} experience files and {len(que_files)} question bank files to process")

    processed = 0
    errors = 0

    # Process experience files
    print("\nProcessing experience files...")
    for file_path in exp_files:
        try:
            # Create corresponding output path
            relative_path = os.path.relpath(file_path, "db/exp")
            output_dir = os.path.join("db/csv/exp", os.path.splitext(relative_path)[0])
            if convert_excel_to_csv(file_path, output_dir):
                processed += 1
            else:
                errors += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            errors += 1

    # Process question bank files
    print("\nProcessing question bank files...")
    for file_path in que_files:
        try:
            # Create corresponding output path
            relative_path = os.path.relpath(file_path, "db/que")
            output_dir = os.path.join("db/csv/que", os.path.splitext(relative_path)[0])
            if convert_excel_to_csv(file_path, output_dir):
                processed += 1
            else:
                errors += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            errors += 1

    print(f"\nProcessing complete!")
    print(f"Successfully processed: {processed} files")
    print(f"Errors encountered: {errors} files")
    print(f"Total files: {total_files}")

if __name__ == "__main__":
    # Change to the script's directory if needed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    process_all_excel_files()