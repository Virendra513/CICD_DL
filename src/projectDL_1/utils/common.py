import os
from box.exceptions import BoxValueError
import yaml
from src.projectDL_1 import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.value_error(f"yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list[Path]): A list of paths to the directories to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory: {path} created successfully")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The dictionary to be saved as a JSON file.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"JSON file: {path} saved successfully")

@ensure_annotations
def load_json(path: Path) -> dict: 
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): The path to the JSON file.
    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    with open(path) as json_file:
        content = json.load(json_file)
        logger.info(f"JSON file: {path} loaded successfully")
        return content
    
@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): The data to be saved as a binary file.
        path (Path): The path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file: {path} saved successfully")    
     
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib and returns its contents.

    Args:
        path (Path): The path to the binary file.
    Returns:
        Any: The contents of the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file: {path} loaded successfully")
    return data