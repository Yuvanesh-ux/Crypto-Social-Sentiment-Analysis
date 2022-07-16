'''Package setup file'''
from setuptools import setup, find_packages

setup(
    name='Tether',
    version='0.0.1',
    url='https://github.com/Yuvanesh-ux/Crypto-Social-Sentiment-Analysis',
    description='Extracting Semantic meaning from Crypto Social Media',
    packages=find_packages(),
    install_requires=[
        'black',
        'isort',
        'transformers'
    ],
    include_package_data=True
)