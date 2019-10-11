import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitandpip",
    version="0.0.1",
    author="arocketman",
    author_email="and.capuano@gmail.com",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/arocketman/git-and-pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
