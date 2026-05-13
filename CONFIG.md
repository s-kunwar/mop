# MOP Configuration Guide

## Overview

This document provides comprehensive guidance for configuring and customizing the Machine for Organizational Processing (MOP) system to meet specific organizational requirements. MOP's modular architecture allows extensive customization while maintaining core processing capabilities.

## Configuration Files Structure

```
config/
├── system.json                 # Core system configuration
├── processing_rules.json       # Data processing rules and standards
├── format_mappings.json        # File format to processing module mappings
├── validation_criteria.json    # Data validation standards
├── cleaning_standards.json     # Data cleaning and standardization rules
├── output_formats.json         # Export and output configuration
├── security_settings.json      # Security and compliance configuration
└── integration_configs/        # External system integration settings
    ├── database.json          # Database connection settings
    ├── cloud_storage.json     # Cloud storage configurations
    ├── api_endpoints.json     # API integration settings
    └── monitoring.json        # Monitoring and alerting configuration
```

## Core System Configuration

### System Settings (`system.json`)

```json
{
  "system": {
    "name": "MOP - Machine for Organizational Processing",
    "version": "1.0.0",
    "environment": "production",
    "timezone": "UTC",
    "locale": "en-US",
    "temp_directory": "/tmp/mop_processing",
    "log_level": "INFO",
    "max_concurrent_processes": 4,
    "memory_limit_mb": 2048,
    "timeout_minutes": 30
  },
  "directories": {
    "input_base": "./db",
    "output_base": "./outputs",
    "scripts": "./scripts",
    "documentation": "./docs",
    "logs": "./logs"
  },
  "performance": {
    "batch_size": 50,
    "retry_attempts": 3,
    "retry_delay_seconds": 5,
    "progress_update_interval": 10
  }
}
```

### Processing Rules (`processing_rules.json`)

```json
{
  "file_classification": {
    "categories": {
      "structured_data": {
        "extensions": [".xlsx", ".xls", ".csv"],
        "priority": 1,
        "processing_module": "structured_extractor"
      },
      "documents": {
        "extensions": [".pdf", ".docx", ".doc"],
        "priority": 2,
        "processing_module": "document_processor"
      },
      "images": {
        "extensions": [".jpg", ".png", ".tiff"],
        "priority": 3,
        "processing_module": "image_analyzer"
      }
    }
  },
  "workflow_priorities": {
    "high_priority_extensions": [".xlsx", ".csv"],
    "medium_priority_extensions": [".pdf", ".docx"],
    "low_priority_extensions": [".jpg", ".png"]
  },
  "error_handling": {
    "skip_corrupted_files": true,
    "log_detailed_errors": true,
    "send_alerts_for_critical_errors": true
  }
}
```

## Data Format and Standardization Configuration

### Format Mappings (`format_mappings.json`)

```json
{
  "column_name_mappings": {
    "experience_files": {
      "Name": "entity_name",
      "USN": "entity_id",
      "Aptitude Test": "process_description",
      "JAM": "status_field",
      "Interview": "process_details",
      "Technical Subjects": "technical_content",
      "Email": "contact_information",
      "Contact Number": "contact_information",
      "CGPA": "numerical_values",
      "Company Name": "category_name",
      "Package": "standardized_values",
      "No. of rounds & Names of those": "process_details",
      "Questions asked during F2F interview": "contextual_questions",
      "Feedback if any": "additional_metadata",
      "Link for Offer Letter/Mail Confirmation Upload": "confirmation_link"
    },
    "question_banks": {
      "Sno": "record_id",
      "S.No": "record_id",
      "Company name": "source_entity",
      "Name of the Company/Drive": "source_entity",
      "Personal interaction": "contextual_questions",
      "Technical Questions": "technical_content",
      "Programming questions": "programming_content"
    }
  },
  "data_format_standards": {
    "package_values": {
      "standard_format": "{value:.2f} LPA",
      "validation_pattern": "^\\d+(\\.\\d{1,2})? LPA$"
    },
    "phone_numbers": {
      "standard_format": "clean_digits_only",
      "validation_pattern": "^\\+?[1-9]\\d{1,14}$"
    },
    "email_addresses": {
      "standard_format": "lowercase",
      "validation_pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    },
    "cgpa_values": {
      "standard_format": "numeric",
      "range_min": 0,
      "range_max": 10,
      "decimal_places": 2
    }
  }
}
```

### Validation Criteria (`validation_criteria.json`)

```json
{
  "data_validation": {
    "email_format": {
      "enabled": true,
      "strict_mode": false,
      "custom_domains_allowed": true
    },
    "phone_number_validation": {
      "enabled": true,
      "country_code_required": false,
      "length_check": {
        "min": 10,
        "max": 15
      }
    },
    "numerical_value_ranges": {
      "cgpa": {
        "min": 0,
        "max": 10
      },
      "package_amount": {
        "min": 0,
        "max": 100
      }
    },
    "text_quality": {
      "max_whitespace_ratio": 0.3,
      "min_content_length": 1,
      "special_character_threshold": 0.1
    }
  },
  "completeness_checks": {
    "required_fields_experience": [
      "entity_name",
      "entity_id",
      "category_name"
    ],
    "required_fields_questions": [
      "record_id",
      "source_entity"
    ]
  }
}
```

## Cleaning Standards Configuration

### Cleaning Rules (`cleaning_standards.json`)

```json
{
  "header_processing": {
    "institutional_rows_to_remove": 6,
    "header_detection_keywords": [
      "Name", "ID", "Date", "Process", "Score", 
      "Company", "Package", "Questions", "Round"
    ],
    "fallback_header_row": 7
  },
  "text_cleaning": {
    "whitespace_normalization": {
      "trim_edges": true,
      "reduce_multiple_spaces": true,
      "normalize_line_breaks": true
    },
    "character_encoding": {
      "target_encoding": "UTF-8",
      "replace_special_chars": true,
      "normalize_case": "lowercase_headers"
    }
  },
  "missing_value_handling": {
    "empty_indicators": ["", "NULL", "N/A", "None", "null", "n/a"],
    "replacement_strategy": "preserve_as_empty",
    "log_missing_values": true
  },
  "duplicate_removal": {
    "check_fields": ["entity_name", "entity_id"],
    "keep_first_occurrence": true,
    "log_duplicates": true
  }
}
```

## Output and Export Configuration

### Output Formats (`output_formats.json`)

```json
{
  "primary_outputs": {
    "csv": {
      "enabled": true,
      "directory": "cleaned_csv",
      "filename_suffix": "_cleaned",
      "encoding": "UTF-8",
      "delimiter": ",",
      "quote_char": "\"",
      "line_terminator": "\n"
    },
    "json": {
      "enabled": true,
      "directory": "structured_json",
      "filename_suffix": "_structured",
      "pretty_print": true,
      "include_metadata": true
    }
  },
  "analytics_exports": {
    "database_ready": {
      "enabled": true,
      "format": "sql_inserts",
      "directory": "database_exports"
    },
    "search_index": {
      "enabled": true,
      "format": "elasticsearch_bulk",
      "directory": "search_indices"
    }
  },
  "knowledge_graph": {
    "nodes_and_edges": {
      "enabled": true,
      "format": "graphml",
      "directory": "knowledge_graph"
    }
  }
}
```

## Security and Compliance Configuration

### Security Settings (`security_settings.json`)

```json
{
  "data_protection": {
    "encryption_at_rest": {
      "enabled": true,
      "algorithm": "AES-256"
    },
    "encryption_in_transit": {
      "enabled": true,
      "protocol": "TLSv1.2"
    }
  },
  "access_control": {
    "authentication_required": true,
    "authorization_model": "role_based",
    "audit_logging": {
      "enabled": true,
      "detail_level": "full"
    }
  },
  "privacy_compliance": {
    "gdpr_compliant": true,
    "data_minimization": {
      "enabled": true,
      "auto_remove_pii": false
    },
    "right_to_deletion": {
      "enabled": true,
      "process_automated": true
    }
  }
}
```

## Integration Configuration

### Database Integration (`integration_configs/database.json`)

```json
{
  "target_databases": {
    "postgresql": {
      "enabled": true,
      "host": "localhost",
      "port": 5432,
      "database": "mop_processed_data",
      "username": "mop_user",
      "password": "secure_password",
      "schema": "public",
      "connection_pool_size": 10
    },
    "mysql": {
      "enabled": false,
      "host": "localhost",
      "port": 3306,
      "database": "mop_data",
      "username": "mop_user",
      "password": "secure_password"
    }
  },
  "export_settings": {
    "batch_insert_size": 1000,
    "table_prefix": "mop_",
    "create_tables_if_not_exist": true
  }
}
```

### Cloud Storage Integration (`integration_configs/cloud_storage.json`)

```json
{
  "aws_s3": {
    "enabled": false,
    "region": "us-east-1",
    "bucket_name": "mop-processing-outputs",
    "access_key_id": "YOUR_ACCESS_KEY",
    "secret_access_key": "YOUR_SECRET_KEY",
    "upload_on_completion": false
  },
  "google_cloud": {
    "enabled": false,
    "project_id": "your-project-id",
    "bucket_name": "mop-outputs",
    "credentials_file": "/path/to/credentials.json"
  },
  "azure_blob": {
    "enabled": false,
    "account_name": "yourstorageaccount",
    "container_name": "mop-outputs",
    "access_key": "your-access-key"
  }
}
```

## Monitoring and Alerting Configuration

### Monitoring Settings (`integration_configs/monitoring.json`)

```json
{
  "logging": {
    "file_logging": {
      "enabled": true,
      "log_directory": "./logs",
      "rotation": {
        "max_size_mb": 50,
        "backup_count": 5
      }
    },
    "console_logging": {
      "enabled": true,
      "level": "INFO"
    }
  },
  "metrics_collection": {
    "prometheus_exporter": {
      "enabled": false,
      "port": 8000
    },
    "statsd": {
      "enabled": false,
      "host": "localhost",
      "port": 8125
    }
  },
  "alerting": {
    "email_alerts": {
      "enabled": false,
      "smtp_server": "smtp.example.com",
      "smtp_port": 587,
      "sender_email": "mop-alerts@example.com",
      "recipient_emails": ["admin@example.com"]
    },
    "slack_notifications": {
      "enabled": false,
      "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
    }
  }
}
```

## Customization Guidelines

### Adding New Data Categories

1. **Define Category in Processing Rules**
   ```json
   {
     "new_category": {
       "extensions": [".ext"],
       "priority": 4,
       "processing_module": "custom_processor"
     }
   }
   ```

2. **Create Column Mappings**
   ```json
   {
     "new_category_files": {
       "Original Field Name": "standardized_field_name"
     }
   }
   ```

3. **Set Validation Criteria**
   ```json
   {
     "new_category_validation": {
       "required_fields": ["field1", "field2"],
       "custom_validations": {}
     }
   }
   ```

### Modifying Data Standards

1. **Update Format Standards**
   ```json
   {
     "custom_field": {
       "standard_format": "your_format",
       "validation_pattern": "your_regex"
     }
   }
   ```

2. **Adjust Cleaning Rules**
   ```json
   {
     "custom_cleaning": {
       "specific_rules": {
         "field_name": "custom_processing_function"
       }
     }
   }
   ```

## Performance Tuning

### Resource Configuration
```json
{
  "performance_tuning": {
    "concurrency_settings": {
      "max_workers": 4,
      "thread_pool_size": 8,
      "async_processing": true
    },
    "memory_management": {
      "chunk_size_rows": 10000,
      "enable_streaming": true,
      "compression_level": 6
    },
    "caching": {
      "enable_result_caching": true,
      "cache_ttl_hours": 24,
      "max_cache_size_gb": 1
    }
  }
}
```

## Environment-Specific Configuration

### Development Environment
```json
{
  "environment": "development",
  "log_level": "DEBUG",
  "max_concurrent_processes": 2,
  "skip_large_files": true
}
```

### Production Environment
```json
{
  "environment": "production",
  "log_level": "INFO",
  "max_concurrent_processes": 8,
  "enable_monitoring": true,
  "backup_outputs": true
}
```

## Best Practices

### Configuration Management
1. **Version Control**: Keep configuration files in version control
2. **Environment Separation**: Use separate configs for dev/staging/prod
3. **Security**: Never store credentials in plain text
4. **Documentation**: Maintain clear documentation of all settings
5. **Testing**: Test configuration changes in staging first

### Security Considerations
1. **Encryption**: Use encrypted configuration files for sensitive data
2. **Access Control**: Restrict access to configuration files
3. **Audit Trails**: Log configuration changes
4. **Credential Management**: Use external secret management systems

This configuration guide enables organizations to fully customize MOP to their specific needs while maintaining the system's core capabilities for transforming organizational archives into structured intelligence.