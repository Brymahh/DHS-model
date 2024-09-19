from setuptools import find_packages, setup
from typing import List

ehyphen = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of packages in requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if ehyphen in requirements:
            requirements.remove(ehyphen)
    
    return requirements


setup(
name='DHS-model',
version='0.0.1',
author='Braimah',
author_email='eseoghenabraimah@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)