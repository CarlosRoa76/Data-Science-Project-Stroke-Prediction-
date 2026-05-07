import os
from tabnanny import verbose
import yaml
from src.stroke_prediction import logger
import json
import joblib
from ensure import ensure_annotations #change to typeguard (@typechecked)
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

#@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Any:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML is empty")
    except Exception as e:
        raise e
    

#@ensure_annotations
def create_directories(path_to_directories: list) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of paths to the directories to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

#@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The dictionary to be saved as JSON.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved at: {path}")


#@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.
    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """

    with open(path) as json_file:
        content = json.load(json_file)

    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)


#@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): The data to be saved.
        path (Path): The path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

#@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.
    Returns:
        Any: The data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data