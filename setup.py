import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mysim800",
    version="0.0.1",
    author="fr3d",
    author_email="fr3d@free",
    description="modified usim800 Python driver module for SIM800.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/Bhagyarsh/usim800l",
    #packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.9",
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires = ['pyserial']
)
