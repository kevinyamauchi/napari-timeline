import os

from setuptools import find_packages, setup

install_requires = [
    line.rstrip()
    for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
]

setup(
    name="napari-timeline",
    install_requires=install_requires,
    version="0.0.1",
    description="A timeline dock widget for napari",
    url="https://github.com/donatolab/poseprocessor",
    license="LGPL",
    packages=find_packages(),
    zip_safe=False,
)
