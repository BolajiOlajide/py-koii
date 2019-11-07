"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

from codecs import open
from os import path


current_path = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(current_path, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="koii",
    version="1.0.0",
    description="A python library to display routes in a flask application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BolajiOlajide/koii-py",
    # Author details
    author="Bolaji Olajide",
    license="MIT",
    keywords="flask routes koii route",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["requests"],
    extras_require={"test": ["coverage"]},
)
