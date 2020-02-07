from setuptools import setup, find_packages
from pathlib import Path
import serializer as s

with (Path(__file__).parents[0] / 'README.md').open() as f:
    long_description = f.read()

setup(
    name="serializer",
    packages=find_packages(),
    include_package_data=True,
    version=s.__version__,
    description=s.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=s.__author__,
    author_email=s.__email__,
    url=s.__url__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
    ],
)
