import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='scicat',
    version='0.3',
    author="Gareth Murphy",
    author_email="garethcmurphy@gmail.com",
    description="a scicat search package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garethcmurphy/scicat_pkg",
    packages=setuptools.find_packages(),
    package_dir={"": "src"},
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
