from setuptools import find_packages,setup 
from typing import List



def get_requirements(file_path:str)->List[str]:
    ''' 
    this function will return a list of requirements'''
    
    hypen = '-e .'
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
            
    return requirements
         
setup(
    name = 'ml_new',
    version = '0.0.1',
    author = 'Yesde',
    author_email = 'divyaselva1498@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

    
)