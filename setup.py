from setuptools import find_packages, setup
from typing import List

HYPEN_E ='-e .'
def get_requirement(file_path: str) -> List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments= file_obj.readline()
        requirments= [req.replace("\n","") for req in requirments]

        if HYPEN_E in requirments:
            requirments.remove(HYPEN_E)
    return requirments

setup(
    name='ml-personal-project',
    version='0.0.1',
    author='jagmeet',
    author_email='jagmeetghotra2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirments.txt')
)