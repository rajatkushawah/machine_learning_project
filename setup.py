from setuptools import setup , find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME='housing-pridictor'
VERSION='0.0.2'
AUTHOR='Rajat kushawah'
DISCRIPTION='THIS IS MY FIRST MACHINE LEARNING PROJECT'
REQUIREMENTS_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    '''
    this function is going to return list of requirment mention in requirements.txt file

    this function is going to return a list which contain name of libraries mentioned in 
    requirements.txt file
    '''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
       return requirement_file.readlines().remove('-e .')

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
discription=DISCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)


