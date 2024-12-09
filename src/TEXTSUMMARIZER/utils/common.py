import yaml
import os
from box.exceptions import BoxValueError
from TEXTSUMMARIZER.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Dict, List, Tuple


@ensure_annotations
def read_yaml_file(file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox (dict-like object with attribute access).
    """
    try:
        # Open and parse the YAML file
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            logger.info(f"Successfully read the file from {file_path}")
        
        # Wrap in ConfigBox for attribute-style access
        config_box = ConfigBox(data)
        return config_box

    except BoxValueError as e:
        logger.error(f"Invalid value in YAML file at {file_path}: {e}")
        raise ValueError(f"Error converting YAML to ConfigBox: {e}")
    
    except yaml.YAMLError as e:
        logger.error(f"YAML parsing error in file {file_path}: {e}")
        raise ValueError(f"Error parsing YAML file: {e}")
    
    except Exception as e:
        logger.error(f"Unexpected error reading file {file_path}: {e}")
        raise RuntimeError(f"Unexpected error: {e}")
    
@ensure_annotations
def create_directory(path_to_dirs,verbose=True):
    """
    Create a directory if it does not exist
    """
    for path in path_to_dirs:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Created a directory at {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists at {path}")



@ensure_annotations
def get_size(path):
    """
    Get the size of the file in bytes
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"