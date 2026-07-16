from marshal import version
from os import name

from setuptools import setup, find_packages
def get_requirements(file_path):
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    name="sachin",
    version="0.1.0",
    author_email="sachinkpsk24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)