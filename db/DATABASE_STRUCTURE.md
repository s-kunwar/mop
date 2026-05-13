# DATABASE STRUCTURE DOCUMENTATION

This document provides comprehensive information about the database structure, file types, and data organization for agents working with this placement preparation repository.

## Overall Repository Structure

```
db/
├── cleaned_csv/           # Cleaned and standardized CSV files (new)
│   ├── exp/              # Cleaned experience files
│   └── que/              # Cleaned question bank files
├── csv/                   # Converted CSV files (intermediate)
│   ├── exp/              # Experience files converted to CSV
│   └── que/              # Question bank files converted to CSV
├── exp/                   # Experience documents from companies
│   ├── 2018-2019/         # Academic year directories
│   ├── 2019-2020/
│   ├── 2020-2021/
│   ├── 2021-2022/
│   ├── 2022-2023/
│   ├── 2023-2024/
│   ├── AY 2024-2025/
│   └── AY 2025-2026/
├── que/                   # Question banks organized by branch
│   ├── AIML/              # Branch directories
│   ├── AInDS/
│   ├── CSE/
│   ├── CV/
│   ├── ECE/
│   ├── EEE/
│   ├── ISE/
│   ├── MBA/
│   ├── MCA/
│   └── ME/
├── aptitude.pdf           # Aptitude preparation materials
└── softskills.pdf         # Soft skills development materials
```

## Detailed Structure Analysis

### Experience Directories (db/exp/)

The experience directory contains company recruitment experiences organized by academic year. Each academic year directory contains multiple company directories with their respective experience documents.

#### Academic Years:
- 2018-2019
- 2019-2020
- 2020-2021 (43 companies)
- 2021-2022
- 2022-2023
- 2023-2024
- AY 2024-2025
- AY 2025-2026

#### File Types in Experience Directories:
1. **PDF files** (.pdf) - Company experience documents
   - Naming convention: `{Company}_{Branch}_Experience.pdf`
   - Examples: `Accenture_EEE_Experience.pdf`, `Cimpress_CSE_Experiances.pdf`
   - Count: 46 files in 2020-2021 alone

2. **Excel files** (.xlsx) - Recruitment process details
   - Naming convention: `{Branch}_{AcademicYear}_Recruitment Process Experience.xlsx` or `{Branch}_Recruitment Process {AcademicYear}_{Date}.xlsx`
   - Examples: `ECE_2020-21_Recruitment Process Experience.xlsx`
   - Count: 31 files in 2020-2021 alone

3. **Image files** (.jpg, .jpeg) - Supporting materials, aptitude questions
   - Often found in company-specific subdirectories like `Eurofins/Aptitude/`
   - Count: 105 files in 2020-2021 alone (.jpg: 93, .jpeg: 12)

#### Company Organization:
Each academic year directory contains multiple company directories with varying numbers of companies per year.

### Question Bank Directories (db/que/)

The question bank directory contains placement preparation materials organized by engineering branch.

#### Branches:
- AIML (Artificial Intelligence and Machine Learning)
- AInDS (Artificial Intelligence and Data Science)
- CSE (Computer Science and Engineering)
- CV (Computer Vision)
- ECE (Electronics and Communication Engineering)
- EEE (Electrical and Electronics Engineering)
- ISE (Information Science and Engineering)
- MBA (Master of Business Administration)
- MCA (Master of Computer Applications)
- ME (Mechanical Engineering)

#### File Types in Question Bank Directories:
1. **Excel files** (.xlsx) - Question banks and placement test materials
   - Naming convention: `PTQB {AcademicYear}_{Branch}.xlsx` or similar
   - Count: 31 files

2. **Word documents** (.docx) - Question banks and placement materials
   - Naming convention: `Placement_ Question_Bank_{Branch}_{AcademicYear}.docx` or similar
   - Examples: `Placement_ Question_Bank_CSE_20-21.docx`
   - Count: 25 files

3. **PDF files** (.pdf) - Question banks and test materials
   - Count: 13 files

4. **PowerPoint presentations** (.ppt) - Lecture materials
   - Count: 1 file

5. **Word documents** (.doc) - Legacy question banks
   - Count: 1 file

## File Type Summary

| File Extension | Count | Description |
|----------------|-------|-------------|
| .pdf | 319 | Experience documents, aptitude materials, question banks |
| .xlsx | 166 | Recruitment process details, question banks |
| .jpg | 93 | Supporting images, aptitude questions |
| .docx | 80 | Question banks, experience documents |
| .jpeg | 12 | Supporting images |
| .ppt | 1 | Lecture presentation |
| .doc | 1 | Legacy document |
| .odt | 1 | Open document format experience |

## Data Organization Patterns

### Naming Conventions:
1. Experience documents: `{Company}_{Branch}_Experience.pdf`
2. Recruitment process: `{Branch}_{AcademicYear}_Recruitment Process Experience.xlsx` or `{Branch}_Recruitment Process {AcademicYear}_{Date}.xlsx`
3. Question banks: `Placement_ Question_Bank_{Branch}_{AcademicYear}.docx` or `PTQB {AcademicYear}_{Branch}.xlsx`
4. Academic years: `YYYY-YYYY` format (e.g., `2020-2021`) or `AY YYYY-YYYY` format
5. CSV files: `{sheet_name}.csv` (derived from Excel sheet names)

### Directory Structure Logic:
1. **Temporal Organization**: Materials are grouped by academic year
2. **Categorical Organization**: Experience vs. Question Banks
3. **Branch-based Organization**: Question banks are organized by engineering branch
4. **Company-based Organization**: Experience documents are organized by company within academic years
5. **Sheet-based Organization**: Each Excel sheet is converted to a separate CSV file

## Common File Access Patterns

### Finding Experience Documents:
- Path: `db/exp/{academic_year}/{company_name}/{document}.{extension}`
- Example: `db/exp/2020-2021/Accenture/Accenture_EEE_Experience.pdf`

### Finding Question Banks:
- Path: `db/que/{branch}/{academic_year}/{document}.{extension}`
- Example: `db/que/CSE/2020-21/Placement_ Question_Bank_CSE_20-21.docx`

### Finding General Preparation Materials:
- Path: `db/{document}.{extension}`
- Examples: `db/aptitude.pdf`, `db/softskills.pdf`

### Finding CSV Files:
- Path: `db/csv/{category}/{academic_year}/{subdirectory}/{sheet_name}.csv`
- Examples: 
  - `db/csv/exp/2020-2021/Accenture/ECE_2020-21_Recruitment Process Experience/ACCENTURE.csv`
  - `db/csv/que/CSE/2023-24/CSE_ technical and programming questions placement 2023-24/programming_and_technical_quest.csv`

## Data Categories

### 1. Company Experience Documents
- Content: Student experiences during recruitment process
- Formats: PDF, Excel
- Purpose: Understanding recruitment patterns, interview questions, selection process

### 2. Question Banks
- Content: Practice questions for placement tests
- Formats: Word documents, Excel spreadsheets, PDFs
- Purpose: Preparation for aptitude tests, technical tests

### 3. Aptitude Materials
- Content: Aptitude preparation resources
- Formats: PDF
- Purpose: General aptitude skill development

### 4. Soft Skills Materials
- Content: Communication and soft skills development resources
- Formats: PDF
- Purpose: Personality development for interviews and group discussions

### 5. Supporting Images
- Content: Screenshots, aptitude question images, diagrams
- Formats: JPG, JPEG
- Purpose: Visual aids for understanding concepts

## Maintenance Guidelines for Agents

1. **File Organization**: Maintain the existing directory structure when adding new materials
2. **Naming Consistency**: Follow established naming conventions
3. **File Format Standards**: Use appropriate formats (PDF for documents, Excel for data, Word for text-heavy content)
4. **Academic Year Grouping**: Ensure materials are placed in correct academic year directories
5. **Branch Categorization**: Place question banks in appropriate branch directories
6. **Company Grouping**: Organize experience documents by company within academic years

## Search and Access Patterns

### For Experience Documents:
1. Navigate to `db/exp/{academic_year}`
2. Find the company directory
3. Access PDF or Excel files with experience information

### For Question Banks:
1. Navigate to `db/que/{branch}`
2. Find the academic year directory
3. Access Word, Excel, or PDF question bank documents

### For General Materials:
1. Access directly from `db/` root directory
2. `aptitude.pdf` and `softskills.pdf` contain general preparation materials

## CSV Conversion Information

All Excel files have been converted to CSV format and stored in the `db/csv/` directory. This conversion maintains the original directory structure while providing text-based access to the data.

### Conversion Process:
- **Script**: `extract_excel_to_csv.py` (located in the root directory)
- **Method**: Each Excel sheet is converted to a separate CSV file
- **Data Preservation**: All content is preserved with appropriate column name cleaning
- **Error Handling**: Files with processing errors are logged and skipped
- **Statistics**: 166 Excel files converted to 1,258 CSV files across 236 directories

### Benefits of CSV Format:
1. **Interoperability**: Can be opened in any spreadsheet application or text editor
2. **Searchability**: Text-based format allows for easy searching and parsing
3. **Version Control**: Better compatibility with version control systems
4. **Data Analysis**: Easier to process programmatically for data analysis
5. **Accessibility**: Can be read without proprietary software

For detailed conversion statistics and process information, see `db/CSV_CONVERSION_SUMMARY.md`.

## Cleaned CSV Data Information

The CSV files have been further cleaned and standardized and stored in the `db/cleaned_csv/` directory. This cleaning process improves data quality and consistency for better integration with other subsystems.

### Cleaning Process:
- **Script**: `clean_csv_data.py` (located in the root directory)
- **Method**: Standardizes column names, cleans data formats, and handles missing values
- **Data Enhancement**: Standardizes package values, phone numbers, emails, and CGPA formats
- **Error Handling**: Files with processing errors are logged and skipped
- **Statistics**: 1,258 CSV files cleaned across 236 directories

### Benefits of Cleaned Data:
1. **Consistent Structure**: Standardized column names and data formats across all files
2. **Improved Data Quality**: Cleaned and validated data formats
3. **Better Integration**: More suitable for integration with analytics and other systems
4. **Enhanced Searchability**: Consistent naming makes data easier to search and parse
5. **Data Validation**: Email, phone number, and package formats have been validated

For detailed cleaning statistics and process information, see `db/CLEANED_CSV_SUMMARY.md`.