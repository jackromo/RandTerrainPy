from setuptools import setup


setup(
    name="RandTerrainPy",
    version="0.0.0",
    url="http://github.com/jackromo/RandTerrainPy",
    license="MIT",
    description="Random terrain generator for Python",
    author="Jack Romo",
    author_email="sharrackor@gmail.com",
    platforms="any",
    packages=['randterrainpy'],
    install_requires=[
        "sphinx>=1.3.6"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python 2.7"
    ]
)
