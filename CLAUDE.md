# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

This repository contains placement preparation materials organized as follows:

- `db/` - Main database directory containing all resources
  - `exp/` - Company experience documents organized by academic year
    - `2018-2019/`, `2019-2020/`, `2020-2021/`, etc. - Academic years
      - Company-specific directories containing experience PDFs and recruitment process documents
  - `que/` - Question banks organized by branch
    - `CSE/`, `ECE/`, `EEE/`, etc. - Branch-specific directories
      - Academic year directories containing question bank documents
  - `aptitude.pdf` - Aptitude preparation materials
  - `softskills.pdf` - Soft skills development materials

For comprehensive details about the database structure, file types, and data organization, refer to `db/DATABASE_STRUCTURE.md`.

## Common Development Tasks

### Adding New Experience Documents

1. Create a directory for the company under the appropriate academic year in `db/exp/`
2. Add experience documents (PDF format) and recruitment process documents (Excel format)
3. Follow the naming convention: `{Company}_{Branch}_Experience.pdf` and `{Branch}_{AcademicYear}_Recruitment Process Experience.xlsx`

### Adding New Question Banks

1. Add question bank documents to the appropriate branch and academic year directory in `db/que/`
2. Follow the naming convention: `Placement_Question_Bank_{Branch}_{AcademicYear}.docx`

### Organizing by Academic Year

Academic years are represented in the format `YYYY-YYYY` (e.g., `2020-2021`) and should be placed in the appropriate directories.

## File Formats

- Experience documents: PDF and Excel formats
- Question banks: Word documents (.docx), Excel spreadsheets (.xlsx), and PDFs
- Aptitude and soft skills: PDF format
- Supporting materials: Images (.jpg, .jpeg)

## Common Operations

### Finding Experience Documents
To find experience documents for a specific company:
- Navigate to `db/exp/{academic_year}/{company_name}/`

### Finding Question Banks
To find question banks for a specific branch:
- Navigate to `db/que/{branch}/{academic_year}/`

## Maintenance Guidelines

1. Keep documents organized by academic year and branch
2. Maintain consistent naming conventions
3. Ensure all documents are in the appropriate format
4. Regularly update the repository with new placement season materials
5. Refer to `db/DATABASE_STRUCTURE.md` for comprehensive understanding of the data organization