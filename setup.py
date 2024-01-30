from setuptools import (setup, find_packages)

with open("README.md") as file:
    read_me_description = file.read()
excluded_packages = ['infra', 'config', 'utils', 'tests']
setup(
    name="jokr-library",
    version="2.0.0",
    author="Esteban Bobbiesi",
    author_email="esteban.bobbiesi@pinapp.tech",
    description="This is an api automation tools package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://InDigitalpe@dev.azure.com/InDigitalpe/JOKR/_git/jokr_lib",
    packages=find_packages(include=['modules']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
