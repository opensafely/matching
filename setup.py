import os
from setuptools import setup, find_packages
#setup()

with open(os.path.join("VERSION")) as f:
    version = f.read().strip()

setup(
    name="opensafely-matching",
    version=version,
    packages=find_packages(),
    url="https://github.com/opensafely/matching",
    author="OpenSAFELY",
    author_email="tech@opensafely.org",
    python_requires=">=3.7",
    install_requires=["pandas"],
    classifiers=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
)