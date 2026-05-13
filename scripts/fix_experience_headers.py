import pandas as pd
import os
import glob

def fix_experience_file_headers(input_path, output_path):
    """Fix experience file headers by removing institutional information"""
    try:
        print(f"Fixing headers for: {input_path}")

        # Load CSV file
        df = pd.read_csv(input_path)

        # Skip empty files
        if df.empty:
            print(f"  Skipping empty file: {input_path}")
            return True

        # For experience files, we need to find the actual header row
        # Look for the row that contains the real headers (usually around row 7)
        header_row_index = None
        for i, row in df.iterrows():
            # Check if this row contains typical header names
            if any(str(cell) in ['Name', 'USN', 'Aptitude Test', 'JAM', 'Interview', 'Email', 'Contact Number', 'CGPA', 'Company Name', 'Package'] for cell in row.astype(str)):
                header_row_index = i
                break

        # If we found the header row, use it
        if header_row_index is not None:
            # Set the header row as column names
            df.columns = df.iloc[header_row_index].values
            # Remove all rows up to and including the header row
            df = df.iloc[header_row_index + 1:].reset_index(drop=True)

        # Remove completely empty rows
        df = df.dropna(how='all')

        # Remove completely empty columns
        df = df.dropna(axis=1, how='all')

        # Create output directory
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save fixed CSV
        df.to_csv(output_path, index=False)
        print(f"  Saved: {output_path}")

        return True
    except Exception as e:
        print(f"Error fixing {input_path}: {e}")
        return False

def fix_all_experience_files():
    """Fix headers for all experience files"""
    print("Starting experience file header fixing process...")

    # Find all experience files that need fixing
    exp_files = glob.glob("db/cleaned_csv/exp/**/*.csv", recursive=True)

    print(f"Found {len(exp_files)} experience files to fix")

    processed = 0
    errors = 0

    for file_path in exp_files:
        try:
            if fix_experience_file_headers(file_path, file_path):
                processed += 1
            else:
                errors += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            errors += 1

    print(f"\nHeader fixing process complete!")
    print(f"Successfully processed: {processed} files")
    print(f"Errors encountered: {errors} files")

if __name__ == "__main__":
    fix_all_experience_files()