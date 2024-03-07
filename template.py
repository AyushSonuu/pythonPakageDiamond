import os
from pathlib import Path
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s",
)

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":
        break

logging.info(f"creating Project by name : {project_name}")

list_of_files = [
    "README.md",
    ".gitignore",
    "LICENSE",
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating directory at: {file_dir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) != 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"creating new file at: {filepath} for file: {filename}")
    else:
        logging.info(f"file already exists at: {filepath} for file: {filename}")
    
