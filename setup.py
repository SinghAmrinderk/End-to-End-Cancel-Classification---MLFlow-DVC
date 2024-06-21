'''
The setuptools library in Python is a package development utility that helps in the packaging, distribution, and installation of Python packages and local packages. 

setup: A function provided by setuptools that is used to configure the package. It takes various arguments that define the package metadata and options.

find_packages: A utility provided by setuptools that automatically discovers all packages and subpackages within a directory. It returns a list of all Python packages that should be included in the distribution.

'''

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney_Disease_Clasification_MLFlow_DVC"  ## GitHub repository name
AUTHOR_USER_NAME = "SinghAmrinderk"  ## GitHub user name
SRC_REPO = "cnnClassifier"           ## Project Name
AUTHOR_EMAIL = "singhamrinder50@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)