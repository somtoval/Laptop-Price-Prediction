# Importing modules that help create a package
from setuptools import find_packages, setup
# Importing List for annotation
from typing import List

# This variable stores a character "-e ." which triggers this setup.py file, so we have to remove it from the list of modules to install
HYPHEN_E_DOT = '-e .'

# The
# This function takes in an argument which is a file path in string form and is to return a list of strings
def get_requirements(file_path:str)->List[str]:
    # Opens the file path obj
    with open(file_path) as file_obj:
        # Reading the file obj line by line
        requirements = file_obj.readlines()
        # Here we remove the newline character for the requirements as they were typed in different lines
        requirements = [req.replace("\n","") for req in requirements]

        # Removing the "-e ." so that we don't return it as a requirement because it is just used to trigger setup.py
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements