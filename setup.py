import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="common_cnv_finder",
    version="0.0.1",
    author="Ava Papetti",
    author_email="avapapetti@gmail.com",
    description="A package that can be used to detect copy number variants (CNVs) found within two different individuals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avapapetti/project_spring_2020",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)