# Placement Preparation Data Repository

This repository contains placement preparation materials that have been processed and cleaned to provide consistent, high-quality data for integration with other systems.

## Repository Overview

The repository contains placement preparation materials organized in a structured hierarchy:

```
.
├── db/                          # Main database directory
│   ├── cleaned_csv/            # Final cleaned and standardized CSV files
│   │   ├── exp/                # Experience files (recruitment process data)
│   │   └── que/                # Question bank files
│   ├── csv/                    # Converted CSV files (intermediate stage)
│   │   ├── exp/                # Experience files converted from Excel
│   │   └── que/                # Question bank files converted from Excel
│   ├── exp/                    # Original experience documents (Excel and PDF)
│   ├── que/                    # Original question banks (Excel, Word, PDF)
│   ├── aptitude.pdf            # Aptitude preparation materials
│   └── softskills.pdf          # Soft skills development materials
├── scripts/                     # Processing scripts
│   ├── extract_excel_to_csv.py  # Excel to CSV conversion script
│   ├── clean_csv_data.py        # CSV data cleaning script
│   ├── clean_csv_data_improved.py # Improved CSV data cleaning script
│   └── fix_experience_headers.py # Header fixing script
├── README.md                   # This file
├── DATABASE_STRUCTURE.md        # Detailed database structure documentation
├── CSV_CONVERSION_SUMMARY.md    # Summary of Excel to CSV conversion
├── CLEANED_CSV_SUMMARY.md       # Summary of CSV data cleaning
└── FINAL_SUMMARY.md             # Comprehensive final summary
```

## Final Results

### Data Processing Statistics
- **Original Excel Files**: 166 files
- **Converted CSV Files**: 1,258 files
- **Directories Created**: 236 directories
- **Processing Success Rate**: 100% (0 errors)
- **Total Processing Time**: ~12 minutes

### Cleaned Data Structure

#### Experience Files (`db/cleaned_csv/exp/`)
Contain student placement experiences with standardized columns:
1. `student_name`
2. `university_seat_number`
3. `aptitude_test_description`
4. `jam_round_description`
5. `interview_description`
6. `technical_subjects`
7. `email`
8. `contact_number`
9. `cgpa`
10. `company_name`
11. `package_offered`
12. `recruitment_rounds`
13. `interview_questions`
14. `feedback`
15. `confirmation_link`

#### Question Bank Files (`db/cleaned_csv/que/`)
Contain technical interview questions with standardized columns:
1. `serial_number`
2. `company_name`
3. `personal_interaction_questions`
4. `technical_questions`
5. `programming_questions`

## How to Use

### Accessing Cleaned Data
The cleaned and standardized data is available in `db/cleaned_csv/`:

```bash
# Navigate to the repository
cd /path/to/repository

# View experience data for a specific company
head -n 10 db/cleaned_csv/exp/2020-2021/Accenture/ECE_2020-21_Recruitment\ Process\ Experience/ACCENTURE_cleaned.csv

# View question bank data for a specific branch
head -n 10 db/cleaned_csv/que/CSE/2023-24/CSE_\ technical\ and\ programming\ questions\ placement\ 2023-24/programming_and_technical_quest_cleaned.csv
```

### Running the Processing Scripts

#### Prerequisites
```bash
# Install required Python packages
pip install pandas openpyxl
```

#### Convert Excel to CSV
```bash
python scripts/extract_excel_to_csv.py
```

#### Clean CSV Data
```bash
python scripts/clean_csv_data.py
```

#### Fix Experience File Headers
```bash
python scripts/fix_experience_headers.py
```

#### Run All Processing Steps
```bash
# Run all scripts in sequence
python scripts/extract_excel_to_csv.py
python scripts/clean_csv_data.py
python scripts/fix_experience_headers.py
```

## Data Quality Improvements

### Standardization
- Consistent column names across all 1,258 files
- Standardized data formats (package values, phone numbers, emails, CGPA)
- Proper handling of missing values

### Validation
- Email format validation and cleaning
- Phone number format standardization
- Package value normalization to "X.XX LPA" format
- CGPA value normalization to numeric format

### Enhancement
- Removal of institutional information rows from experience files
- Elimination of empty rows and columns
- Text cleaning (removal of extra whitespace)
- Header promotion to proper column names

## Benefits for Subsystem Integration

1. **Consistent Structure**: All files have standardized column names and structure
2. **Improved Data Quality**: Cleaned data with validated formats
3. **Better Searchability**: Consistent naming makes data easier to search and parse
4. **Enhanced Interoperability**: Cleaned CSV files can be easily integrated with other systems
5. **Reduced Preprocessing**: Minimal additional cleaning required for integration

## Documentation

- **DATABASE_STRUCTURE.md**: Detailed information about the database structure
- **CSV_CONVERSION_SUMMARY.md**: Statistics and details about the Excel to CSV conversion
- **CLEANED_CSV_SUMMARY.md**: Statistics and details about the CSV data cleaning process
- **FINAL_SUMMARY.md**: Comprehensive final summary of the entire process

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit your changes
5. Push to the branch
6. Create a pull request

## License

This repository contains educational materials for placement preparation. Please respect the original authors and use the materials appropriately.

## Support

For issues or questions about the data processing pipeline, please open an issue in this repository.