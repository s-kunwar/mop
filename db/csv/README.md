# CSV Files Directory

This directory contains all Excel files from the placement preparation repository converted to CSV format.

## Structure

The directory structure mirrors the original Excel file organization:

```
csv/
├── exp/     # Experience files (recruitment process data)
│   ├── 2018-2019/
│   ├── 2019-2020/
│   ├── 2020-2021/
│   └── ...   # Academic years
└── que/     # Question bank files
    ├── AIML/
    ├── AInDS/
    ├── CSE/
    ├── ECE/
    ├── EEE/
    └── ...   # Engineering branches
```

## Conversion Details

- Each Excel file has been converted to CSV format
- Each sheet in an Excel file becomes a separate CSV file
- Original directory structure has been preserved
- Column names have been cleaned for better readability
- Empty rows and columns have been removed

## Benefits

1. **Interoperability**: CSV files can be opened in any spreadsheet application or text editor
2. **Searchability**: Text-based format allows for easy searching and parsing
3. **Version Control**: Better compatibility with version control systems
4. **Data Analysis**: Easier to process programmatically for data analysis
5. **Accessibility**: Can be read without proprietary software

## File Naming

CSV files are named after their corresponding Excel sheet names, with special characters removed and spaces replaced with underscores.

## Statistics

- Total CSV files: 1,258
- Directories: 236
- Excel files processed: 166
- Errors: 0

For more information about the conversion process, see `../CSV_CONVERSION_SUMMARY.md`.