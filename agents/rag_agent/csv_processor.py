import pandas as pd
import logging
from typing import List, Dict, Any
from pathlib import Path

class CSVProcessor:
    """
    Processes CSV files containing medical data for RAG ingestion.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("CSV Processor initialized!")
    
    def process_csv(self, csv_path: str) -> List[str]:
        """
        Process CSV file and convert to text chunks for RAG ingestion.
        
        Args:
            csv_path: Path to the CSV file
            
        Returns:
            List of formatted text chunks
        """
        try:
            # Read CSV file
            df = pd.read_csv(csv_path)
            self.logger.info(f"Loaded CSV with {len(df)} rows and {len(df.columns)} columns")
            
            # Get file name for context
            file_name = Path(csv_path).stem
            
            chunks = []
            
            # Create header chunk with metadata
            header_chunk = self._create_header_chunk(df, file_name)
            chunks.append(header_chunk)
            
            # Process each row as a separate chunk
            for idx, row in df.iterrows():
                chunk = self._create_row_chunk(row, idx, file_name)
                chunks.append(chunk)
            
            # Create summary chunk
            summary_chunk = self._create_summary_chunk(df, file_name)
            chunks.append(summary_chunk)
            
            self.logger.info(f"Created {len(chunks)} chunks from CSV file")
            return chunks
            
        except Exception as e:
            self.logger.error(f"Error processing CSV file {csv_path}: {e}")
            raise
    
    def _create_header_chunk(self, df: pd.DataFrame, file_name: str) -> str:
        """Create a header chunk with CSV metadata."""
        columns = ", ".join(df.columns.tolist())
        
        chunk = f"""# Medical Data: {file_name}

## Dataset Information
- **Source**: {file_name}.csv
- **Total Records**: {len(df)}
- **Columns**: {columns}
- **Data Type**: Medical recommendations and information

## Column Descriptions
"""
        
        # Add column info
        for col in df.columns:
            sample_values = df[col].dropna().head(3).tolist()
            chunk += f"- **{col}**: {', '.join(map(str, sample_values))}...\n"
        
        return chunk
    
    def _create_row_chunk(self, row: pd.Series, idx: int, file_name: str) -> str:
        """Create a chunk for each row of data."""
        
        chunk = f"## Medical Record {idx + 1} from {file_name}\n\n"
        
        for col, value in row.items():
            if pd.notna(value):
                # Format different types of medical data
                if any(keyword in col.lower() for keyword in ['medicine', 'drug', 'medication', 'treatment']):
                    chunk += f"**{col}**: {value}\n"
                elif any(keyword in col.lower() for keyword in ['symptom', 'condition', 'disease', 'diagnosis']):
                    chunk += f"**{col}**: {value}\n"
                elif any(keyword in col.lower() for keyword in ['dosage', 'dose', 'frequency', 'duration']):
                    chunk += f"**{col}**: {value}\n"
                else:
                    chunk += f"**{col}**: {value}\n"
        
        chunk += "\n"
        return chunk
    
    def _create_summary_chunk(self, df: pd.DataFrame, file_name: str) -> str:
        """Create a summary chunk with key statistics."""
        
        chunk = f"## Summary Statistics for {file_name}\n\n"
        
        # Basic statistics
        chunk += f"- **Total medical records**: {len(df)}\n"
        
        # Find medicine/drug columns
        medicine_cols = [col for col in df.columns if any(keyword in col.lower() 
                        for keyword in ['medicine', 'drug', 'medication', 'treatment'])]
        
        if medicine_cols:
            chunk += f"- **Medicine/Drug columns**: {', '.join(medicine_cols)}\n"
            
            # Get unique medicines
            for col in medicine_cols:
                unique_medicines = df[col].dropna().unique()
                if len(unique_medicines) <= 20:  # Only show if manageable number
                    chunk += f"- **Unique {col}**: {', '.join(map(str, unique_medicines))}\n"
                else:
                    chunk += f"- **Unique {col}**: {len(unique_medicines)} different entries\n"
        
        # Find condition columns
        condition_cols = [col for col in df.columns if any(keyword in col.lower() 
                         for keyword in ['symptom', 'condition', 'disease', 'diagnosis'])]
        
        if condition_cols:
            chunk += f"- **Condition columns**: {', '.join(condition_cols)}\n"
        
        return chunk
