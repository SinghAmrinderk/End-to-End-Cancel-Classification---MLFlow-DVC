import os
from pathlib import Path
import logging

'''
level=logging.INFO:

This sets the logging level to INFO.
The logging levels in increasing order of severity are: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
By setting the level to INFO, the logger will handle all messages that are at the INFO level and above (i.e., INFO, WARNING, ERROR, and CRITICAL). It will ignore DEBUG messages.
format='[%(asctime)s]: %(message)s:':

This sets the format for the log messages.
%(asctime)s: This placeholder will be replaced by the time the log message was created. The default format is ISO8601 (e.g., "2024-06-20 12:00:00,123").
%(message)s: This placeholder will be replaced by the actual log message.
The format string '[%(asctime)s]: %(message)s:' ensures that each log message is prefixed with a timestamp and is followed by the log message itself, enclosed in square brackets and separated by colons.

'''

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

'''
Package Initialization: An __init__.py file is executed when the package is imported, and it can contain initialization code for the package. This can include setting up variables, importing submodules, or running initialization code 

Namespace Package: By including an __init__.py file, you declare that the directory is a package. This allows you to use the dot notation to import modules from this package, such as import cnnClassifier.utils or from cnnClassifier.components import some_component.

Control over Importing: You can control what gets imported when the package is imported. For example, if you have the following __init__.py file:
# src/cnnClassifier/utils/__init__.py

from .module1 import function1
from .module2 import function2
Then, when you do from cnnClassifier.utils import *, only function1 and function2 will be imported.
'''

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "secret/secret.yaml"
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


for filepath in list_of_files:
    ''' Path - In window system, backword slash will be provided while mentioning the path so it will take care of this according to operationg system'''
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        '''
        When exist_ok is set to True (which is the default), os.makedirs() will not raise an error if the directory already exists. 
        It will simply proceed without attempting to create the directory again.
        If exist_ok were set to False and the directory already existed, os.makedirs() would raise a FileExistsError.
        '''
        os.makedirs(filedir, exist_ok=True)  
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        '''
        os.path.exists(filepath) function is used to check whether a file or directory exists at a given path. 
        It returns True if the file or directory exists, and False otherwise.
        '''
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        '''
        This code opens a file specified by the variable filepath in write mode ("w"). Using the with statement is a good practice because it automatically handles closing the file 
        when you're done with it, even if an error occurs within the block. If the file specified by filepath doesn't exist, this code will create a new file with that name. 
        The "w" mode in the open() function signifies writing mode, which will create a new file if it doesn't exist or truncate the existing file to zero length if it does exist.
        '''
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")