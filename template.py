import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:]')

project_name = "ChickenDisease"

list_of_files = [
    ".github/workflows/.gitkeep",  # For CI/CD Deployment ( .gitkeep is added as empty folders are not committed in github)
    f"src/{project_name}/__init__.py", # Will act as a local package cause of __init__.py
    f"src/{project_name}/components/__init__.py", # Components is oing to be another local package'
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py",  # Contain programs for reading, downloading and saving files used in whole project
    f"src/{project_name}/config/__init__.py",
    f'src/{project_name}/config/configuration.py', # Contains all the configurations. Create paths to variable, read and create directories
    f'src/{project_name}/pipeline/__init__.py',   # Contains all the pipeline configuration for every part of the project
    f'src/{project_name}/entity/__init__.py',   
    f'src/{project_name}/entity/config_entity.py', # Contains the variables that are used to stored the paths of files/folder nedded in a particular part
    f'src/{project_name}/constants/__init__.py',  # Stores yaml files paths
    'config/config.yaml',   # Stores paths of files/directories used in every part of the project
    'main.py',  # Stores all the pipelines 
    'dvc.yaml',  # Used for MLOPS tool to monitor the pipelines.
    'params.yaml',  # Contains parameter used.
    'requirements.txt',
    'setup.py',  # Will be used to setup the project
    'research/trials.ipynb',  # First experiments will be performed here, then will be written in the official files.
    'templates/index.html'  # FOr Web app
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0) :
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file {filename}')
            
    else:
        logging.info(f'File {filename} already exists')