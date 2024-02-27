from setuptools import setup,find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements

setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='Sumit_Singh',
    author_email='sumitttanwar4169@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages() 
)