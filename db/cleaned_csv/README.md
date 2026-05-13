# Cleaned CSV Files Directory

This directory contains all CSV files from the placement preparation repository that have been cleaned and standardized for better integration with other subsystems.

## Structure

The directory structure mirrors the original CSV file organization:

```
cleaned_csv/
├── exp/     # Cleaned experience files (recruitment process data)
│   ├── 2018-2019/
│   ├── 2019-2020/
│   ├── 2020-2021/
│   └── ...   # Academic years
└── que/     # Cleaned question bank files
    ├── AIML/
    ├── AInDS/
    ├── CSE/
    ├── ECE/
    ├── EEE/
    └── ...   # Engineering branches
```

## Cleaning Details

- Each CSV file has been cleaned and standardized
- Column names have been standardized across all files
- Data formats have been cleaned and validated
- Missing values have been handled consistently
- Files are named with "_cleaned" suffix to distinguish from original CSV files

## Standardized Column Names

### Experience Files
1. student_name
2. university_seat_number
3. aptitude_test_description
4. jam_round_description
5. interview_description
6. technical_subjects
7. email
8. contact_number
9. cgpa
10. company_name
11. package_offered
12. recruitment_rounds
13. interview_questions
14. feedback
15. confirmation_link

### Question Bank Files
1. serial_number
2. company_name
3. personal_interaction_questions
4. technical_questions
5. programming_questions

## Benefits

1. **Consistent Structure**: All files have standardized column names and structure
2. **Improved Data Quality**: Cleaned data with standardized formats
3. **Better Integration**: More suitable for integration with analytics and other systems
4. **Enhanced Searchability**: Consistent naming makes data easier to search and parse
5. **Data Validation**: Email, phone number, and package formats have been validated

## File Naming

Cleaned CSV files are named after their corresponding original CSV files with "_cleaned" appended to the filename.

## Statistics

- Total cleaned CSV files: 1,258
- Directories: 236
- CSV files processed: 1,258
- Errors: 0

For more information about the cleaning process, see `../CLEANED_CSV_SUMMARY.md`.