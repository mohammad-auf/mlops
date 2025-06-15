from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requiremnets(filepath:str)-> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = [req.replace('\n', '') for req in file_obj.readlines()]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlops',
    version='0.0.1',
    author='auf',
    author_email='mohammadauf11@gmail.com',
    packages=find_packages(),
    include_dirs=get_requiremnets("requiremnets.txt")
)