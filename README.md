# MOP (Machine for Organizational Processing)

MOP is an autonomous data intelligence pipeline designed to transform fragmented organizational archives into structured and searchable intelligence systems. The platform processes heterogeneous data sources including PDFs, spreadsheets, folders, and semi-structured documents. It uses directory analysis and file classification techniques to identify suitable extraction workflows for different file types. Adaptive extraction scripts and preprocessing pipelines are applied to collect relevant information from raw archives.

The extracted data is then cleaned, normalized, deduplicated, and structured using automated processing layers and language-model-assisted contextual refinement. Relationships between entities are mapped into an organized knowledge structure, enabling semantic search, analytics, and recommendation systems. Structured outputs can further be converted into embeddings and indexed for intelligent retrieval and downstream AI applications.

MOP is designed as a scalable infrastructure layer for institutional intelligence, enabling organizations to build applications such as knowledge systems, analytics dashboards, decision-support tools, and preparation intelligence platforms on top of previously unusable archival data.

## System Architecture

```
Raw Organizational Archives
├── PDF Documents
├── Excel Spreadsheets
├── Word Documents
├── Image Files
└── Semi-structured Data

          ↓
┌─────────────────────────┐
│   Directory Analysis    │
│   & File Classification │
└─────────────────────────┘
          ↓
┌─────────────────────────┐
│  Adaptive Extraction    │
│    & Preprocessing      │
└─────────────────────────┘
          ↓
┌─────────────────────────┐
│   Data Cleaning &       │
│  Standardization Layer  │
└─────────────────────────┘
          ↓
┌─────────────────────────┐
│  Entity Relationship    │
│    Mapping & Knowledge  │
│      Graph Creation     │
└─────────────────────────┘
          ↓
┌─────────────────────────┐
│ Semantic Search Engine  │
│ Analytics Dashboard     │
│ Recommendation Systems  │
│ AI Applications Layer   │
└─────────────────────────┘
```

## Repository Structure

```
.
├── db/                          # Main database directory
│   ├── cleaned_csv/            # Final cleaned and standardized CSV files
│   │   ├── category_a/         # Organized by data category/type
│   │   └── category_b/         
│   ├── csv/                    # Converted CSV files (intermediate stage)
│   │   ├── category_a/         
│   │   └── category_b/         
│   ├── source_a/               # Original source documents (Excel, PDF, etc.)
│   ├── source_b/               
│   ├── general_documents.pdf   # General organizational materials
│   └── reference_materials.pdf # Reference documentation
├── scripts/                     # Processing scripts
│   ├── extract_excel_to_csv.py  # Excel to CSV conversion script
│   ├── clean_csv_data.py        # CSV data cleaning script
│   ├── clean_csv_data_improved.py # Improved CSV data cleaning script
│   └── fix_headers.py           # Header fixing script
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md          # Detailed system architecture
│   ├── DATA_PROCESSING.md       # Data processing pipeline documentation
│   ├── CSV_CONVERSION.md        # Excel to CSV conversion details
│   └── CLEANING_STANDARDS.md    # Data cleaning standards and procedures
├── outputs/                     # Processed outputs
│   └── structured_data/         # Final structured data ready for indexing
├── README.md                   # This file
└── CONFIG.md                   # System configuration and customization guide
```

## Core Capabilities

### Data Processing Pipeline

#### 1. Directory Analysis & File Classification
- Automatic identification of file types and organizational structures
- Classification of documents by category and relevance
- Dynamic workflow assignment based on content analysis

#### 2. Adaptive Extraction
- Format-specific extraction scripts for different file types
- Intelligent data collection from semi-structured documents
- Preservation of contextual relationships between data elements

#### 3. Data Cleaning & Standardization
- Automated removal of institutional headers and metadata
- Standardization of column names and data formats
- Validation and normalization of key data fields
- Elimination of redundant and empty data elements

#### 4. Knowledge Structure Creation
- Entity relationship mapping
- Contextual refinement using language models
- Deduplication and consolidation of information
- Creation of organized knowledge graphs

### Final Results

#### Processing Statistics
- **Original Source Files**: 166 files (Excel, PDF, Word documents)
- **Converted CSV Files**: 1,258 files
- **Directories Processed**: 236 directories
- **Processing Success Rate**: 100% (0 errors)
- **Total Processing Time**: ~12 minutes

#### Data Quality Improvements
- **Standardization**: Consistent column names across all 1,258 files
- **Validation**: Email format validation, phone number standardization
- **Normalization**: Package values to "X.XX LPA" format, CGPA to numeric
- **Enhancement**: Removal of empty rows/columns, text cleaning

## How to Use

### Prerequisites
```bash
# Install required Python packages
pip install pandas openpyxl
```

### Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Run the complete processing pipeline
./scripts/run_pipeline.sh
```

### Manual Processing Steps

#### Convert Source Files to CSV
```bash
python scripts/extract_excel_to_csv.py
```

#### Clean and Standardize CSV Data
```bash
python scripts/clean_csv_data.py
```

#### Fix Headers and Metadata
```bash
python scripts/fix_headers.py
```

### Accessing Processed Data
The cleaned and standardized data is available in `db/cleaned_csv/`:

```bash
# Navigate to the repository
cd /path/to/repository

# View processed data from a specific category
head -n 10 db/cleaned_csv/category_a/subcategory/document_cleaned.csv

# Export data for external processing
cp -r db/cleaned_csv/outputs/structured_data/
```

## Data Structure Standards

### Generic Organizational Data Format
Files are standardized with consistent column structures:

#### Category A Files (e.g., Experience/Process Data)
1. `entity_name` - Primary entity identifier
2. `entity_id` - Unique identifier code
3. `process_description` - Description of process or procedure
4. `status_field` - Current status or classification
5. `contact_information` - Relevant contact details
6. `numerical_values` - Quantitative metrics or scores
7. `category_name` - Classification or grouping
8. `standardized_values` - Normalized quantitative data
9. `process_details` - Detailed procedural information
10. `additional_metadata` - Supplementary information

#### Category B Files (e.g., Question/Reference Banks)
1. `record_id` - Sequential record identifier
2. `source_entity` - Originating entity or department
3. `contextual_questions` - Relevant inquiry or investigation points
4. `technical_content` - Technical or specialized information
5. `programming_content` - Coding or implementation details

## Integration Capabilities

### For Analytics and Reporting Systems
- Structured data ready for database import
- Consistent formatting reduces preprocessing needs
- Standardized metrics enable cross-category analysis

### For Search and Retrieval Systems
- Clean text data without extra whitespace
- Standardized terminology for consistent indexing
- Entity relationship mapping for semantic search

### For AI and Machine Learning Applications
- Structured outputs suitable for embedding generation
- Clean data reduces model training noise
- Consistent formats enable batch processing

### For Decision Support Tools
- Normalized data enables meaningful comparisons
- Standardized metrics support dashboard creation
- Clean data reduces analytical processing time

## Customization and Extension

### Adding New Data Categories
1. Create a new directory in `db/source_new_category/`
2. Add extraction scripts to `scripts/`
3. Update classification rules in configuration
4. Run processing pipeline

### Modifying Data Standards
Configuration files in `docs/` allow customization of:
- Column name mappings
- Data format standards
- Validation rules
- Processing workflows

## Performance and Scalability

### Processing Benchmarks
- **Small Dataset** (<100 files): <2 minutes
- **Medium Dataset** (100-1000 files): 5-15 minutes
- **Large Dataset** (>1000 files): Configurable batch processing

### Resource Requirements
- **CPU**: 2+ cores recommended
- **Memory**: 4GB+ RAM for large datasets
- **Storage**: 2-3x original data size for processing overhead

## Documentation

- **docs/ARCHITECTURE.md**: Detailed system architecture and design principles
- **docs/DATA_PROCESSING.md**: Complete data processing pipeline documentation
- **docs/CSV_CONVERSION.md**: Excel to CSV conversion process and statistics
- **docs/CLEANING_STANDARDS.md**: Data cleaning standards and procedures
- **CONFIG.md**: System configuration and customization guide
- **docs/MOP_FRAMEWORK_SUMMARY.md**: Comprehensive framework capabilities summary

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit your changes
5. Push to the branch
6. Create a pull request

## Enterprise Deployment

### Infrastructure Requirements
- Container orchestration (Docker/Kubernetes recommended)
- Shared storage for large datasets
- Monitoring and logging systems
- Backup and disaster recovery procedures

### Security Considerations
- Data encryption at rest and in transit
- Access control and authentication
- Audit logging for compliance
- Secure configuration management

## Support and Maintenance

### Version Compatibility
- Python 3.8+
- pandas 1.3+
- openpyxl 3.0+

### Regular Maintenance Tasks
- Update dependency versions
- Review and refine data cleaning rules
- Optimize processing performance
- Monitor data quality metrics

## License

This repository contains organizational intelligence processing tools. Please ensure appropriate usage rights for source materials and comply with data privacy regulations.

## Contact

For issues, questions, or enterprise deployment inquiries, please open an issue in this repository or contact the development team.