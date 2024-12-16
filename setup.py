from setuptools import setup, find_packages

setup(
    name="bioactivity_analysis",
    version="1.0.0",
    description="Analyze bioactivity data from PubChem and ChEMBL.",
    author="Anne Deslattes Mays, PhD",
    packages=find_packages(),
    install_requires=[
        "requests",
        "chembl-webresource-client",
        "pandas",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
