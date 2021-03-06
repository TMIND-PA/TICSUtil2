from setuptools import setup, find_packages

setup(
    name="TICSUtil2",
    version="0.7.0",
    description="This package is a library of small functions used in TICS development.",
    author="Sunil Goothy",
    author_email="sunil.goothy@tmeic.in",
    install_requires=[
        "loguru",
        "pyyaml",
    ],
    packages=find_packages(),
)
