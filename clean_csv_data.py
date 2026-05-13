import pandas as pd
import os
import glob
import re
import sys
from pathlib import Path

def standardize_package(package_str):
    """Standardize package format to X.XX LPA"""
    if pd.isna(package_str) or package_str == '' or str(package_str).strip().lower() in ['nan', 'null', 'none']:
        return None

    # Convert to string and clean
    package_str = str(package_str).strip()

    # Handle various formats like "4.5 LPA", "6.5L PA", "4.02 LPA", "7.6 LPA"
    # Extract numeric value
    match = re.search(r'(\d+\.?\d*)', package_str)
    if match:
        try:
            value = float(match.group(1))
            return f"{value:.2f} LPA"
        except ValueError:
            return package_str
    return package_str

def clean_phone_number(phone_str):
    """Clean phone number to consistent format"""
    if pd.isna(phone_str) or phone_str == '' or str(phone_str).strip().lower() in ['nan', 'null', 'none']:
        return None

    # Convert to string and clean
    phone_str = str(phone_str).strip()

    # Remove non-digit characters except +
    cleaned = re.sub(r'[^\d+]', '', phone_str)

    # If it's too short or too long, return as is
    if len(cleaned) < 10 or len(cleaned) > 15:
        return phone_str

    return cleaned

def clean_email(email_str):
    """Clean and validate email format"""
    if pd.isna(email_str) or email_str == '' or str(email_str).strip().lower() in ['nan', 'null', 'none']:
        return None

    # Convert to string and clean
    email_str = str(email_str).strip().lower()

    # Basic email validation
    if '@' in email_str and '.' in email_str:
        return email_str

    return None

def clean_cgpa(cgpa_str):
    """Clean CGPA to numeric format"""
    if pd.isna(cgpa_str) or cgpa_str == '' or str(cgpa_str).strip().lower() in ['nan', 'null', 'none']:
        return None

    # Convert to string and clean
    cgpa_str = str(cgpa_str).strip()

    # Try to extract numeric value
    try:
        # Handle cases like "7.8 CGPA" or "7.8/10"
        match = re.search(r'(\d+\.?\d*)', cgpa_str)
        if match:
            value = float(match.group(1))
            # CGPA should be between 0 and 10
            if 0 <= value <= 10:
                return value
    except ValueError:
        pass

    return cgpa_str

def clean_experience_file(df):
    """Clean experience file data"""
    # Standardize column names
    column_mapping = {
        'Name': 'student_name',
        'USN': 'university_seat_number',
        'Aptitude Test': 'aptitude_test_description',
        'JAM': 'jam_round_description',
        'Interview': 'interview_description',
        'Technical Subjects': 'technical_subjects',
        'Email': 'email',
        'Contact Number': 'contact_number',
        'CGPA': 'cgpa',
        'Company Name': 'company_name',
        'Package': 'package_offered',
        'No. of rounds & Names of those': 'recruitment_rounds',
        'Questions asked during F2F interview': 'interview_questions',
        'Feedback if any': 'feedback',
        'Link for Offer Letter/Mail Confirmation Upload': 'confirmation_link'
    }

    # Apply column mapping for existing columns
    df = df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns})

    # Standardize package format
    if 'package_offered' in df.columns:
        df['package_offered'] = df['package_offered'].apply(standardize_package)

    # Clean phone numbers
    if 'contact_number' in df.columns:
        df['contact_number'] = df['contact_number'].apply(clean_phone_number)

    # Clean emails
    if 'email' in df.columns:
        df['email'] = df['email'].apply(clean_email)

    # Clean CGPA
    if 'cgpa' in df.columns:
        df['cgpa'] = df['cgpa'].apply(clean_cgpa)

    # Remove extra whitespace from string columns
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].apply(lambda x: str(x).strip() if not pd.isna(x) else x)

    return df

def clean_question_bank_file(df):
    """Clean question bank file data"""
    # Standardize column names for question banks
    column_mapping = {
        'Sno': 'serial_number',
        'S.No': 'serial_number',
        'Company name': 'company_name',
        'Name of the Company/Drive': 'company_name',
        'Technical Questions': 'technical_questions',
        'Programming questions': 'programming_questions',
        'Personal interaction': 'personal_interaction_questions',
        'Sno,Name of the Company/Drive,Personal interaction, Technical questions,Programming questions': 'header_row'  # Special case
    }

    # Apply column mapping
    df = df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns})

    # Handle special case where all column names are in one cell
    if 'header_row' in df.columns:
        # Split the header row into separate columns
        df[['serial_number', 'company_name', 'personal_interaction_questions', 'technical_questions', 'programming_questions']] = df['header_row'].str.split(',', expand=True)
        df = df.drop('header_row', axis=1)

    # Remove extra whitespace from string columns
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].apply(lambda x: str(x).strip() if not pd.isna(x) else x)

    return df

def clean_csv_file(input_path, output_path):
    """Clean a CSV file and save the cleaned version"""
    try:
        print(f"Processing: {input_path}")

        # Load CSV file
        df = pd.read_csv(input_path)

        # Skip empty files
        if df.empty:
            print(f"  Skipping empty file: {input_path}")
            return True

        # Determine file type and apply appropriate cleaning
        if 'exp' in input_path.lower():
            # Experience file
            df = clean_experience_file(df)
        elif 'que' in input_path.lower():
            # Question bank file
            df = clean_question_bank_file(df)
        else:
            # Unknown type, apply basic cleaning
            # Remove extra whitespace from string columns
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].apply(lambda x: str(x).strip() if not pd.isna(x) else x)

        # Create output directory
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save cleaned CSV
        df.to_csv(output_path, index=False)
        print(f"  Saved: {output_path}")

        return True
    except Exception as e:
        print(f"Error cleaning {input_path}: {e}")
        return False

def process_all_csv_files():
    """Process all CSV files in db/csv and create cleaned versions"""
    print("Starting CSV data cleaning process...")

    # Count total files to process
    exp_files = glob.glob("db/csv/exp/**/*.csv", recursive=True)
    que_files = glob.glob("db/csv/que/**/*.csv", recursive=True)
    total_files = len(exp_files) + len(que_files)

    print(f"Found {len(exp_files)} experience files and {len(que_files)} question bank files to clean")

    processed = 0
    errors = 0

    # Process experience files
    print("\nCleaning experience files...")
    for file_path in exp_files:
        try:
            # Create corresponding output path
            relative_path = os.path.relpath(file_path, "db/csv")
            output_path = os.path.join("db/cleaned_csv", relative_path)
            # Add "_cleaned" to filename
            output_path = os.path.splitext(output_path)[0] + "_cleaned" + os.path.splitext(output_path)[1]

            if clean_csv_file(file_path, output_path):
                processed += 1
            else:
                errors += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            errors += 1

    # Process question bank files
    print("\nCleaning question bank files...")
    for file_path in que_files:
        try:
            # Create corresponding output path
            relative_path = os.path.relpath(file_path, "db/csv")
            output_path = os.path.join("db/cleaned_csv", relative_path)
            # Add "_cleaned" to filename
            output_path = os.path.splitext(output_path)[0] + "_cleaned" + os.path.splitext(output_path)[1]

            if clean_csv_file(file_path, output_path):
                processed += 1
            else:
                errors += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            errors += 1

    print(f"\nCleaning process complete!")
    print(f"Successfully processed: {processed} files")
    print(f"Errors encountered: {errors} files")
    print(f"Total files: {total_files}")

if __name__ == "__main__":
    # Change to the script's directory if needed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    process_all_csv_files()