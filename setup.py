from setuptools import setup
from typing import List

REQUIREMENTS

def get_requirements_list()->List[str]:
    pass

# Declaring variables for set up functions

projectname="housing_predictor"
version=" 0.0.2"
author="Mahesh"
description=="THIS IS FIRST PROJECT OF HOUSING"
packages=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file

    return This function is gping to return a list which contain name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().pop("-e .")




setup(
name=PROJECT_NAME,
version= VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)



)