from setuptools import setup, find_packages

setup(
    name="tobii_recorder",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "tobii_recorder": ["*.pyd", "*.dll"],
    },
    install_requires=[
        # Add any dependencies here
    ],
    author="Mohammadhossein Salari",
    author_email="mohammadhossein.salari@gmail.com",
    description="A Python wrapper for Tobii Eye Tracker data recording",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mh-salari/tobii_recorder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
    ],
)
