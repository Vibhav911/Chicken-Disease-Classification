# Entity Program
# This program is the written type of the files and directories
from dataclasses import dataclass
from pathlib import Path


# Data Ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path