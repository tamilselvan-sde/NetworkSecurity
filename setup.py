from setuptools import find_packages, setup
from typing import List


def get_requirmetents(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements : List[str] = []
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements.append(requirement)
    except FileNotFoundError:
        print("File not found")
    return requirements

#print(get_requirmetents('requirements.txt'))

setup(
    name="mlproject",
    version="0.0.1",
    author="Tamilselvan",
    author_email="stselvan9095@gmail.com",
    package = find_packages(),
    install_requires = get_requirmetents('requirements.txt')
)