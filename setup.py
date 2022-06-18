from setuptools import setup

with open("README.md", "r", encoding= 'utf-8') as fh:
    long_description = fh.read()

REPO_NAME = 'simple Linear Regression pipeline'
AUTHOR_USE_NAME = "ChanduKReddy99"
AUTHOR_EMAIL = "chanduk.amical@gmail.com"
URL= "https://github.com/ChanduKReddy99/project1"
PYTHON_REQUIRES = '>=3.6'
SRC_REPO= "src"
INSTALL_REQUIRES = [
    'dvc',
    'pandas',
    'scikit-learn',
    'tqdm'
]


setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_USE_NAME,
    author_email=AUTHOR_EMAIL,
    description='Simple Linear Regression pipeline',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=['src'],
    python_requires=PYTHON_REQUIRES,
    license='MIT',
    install_requires=INSTALL_REQUIRES,

)
