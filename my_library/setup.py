from setuptools import setup, find_packages

setup(
    name='my_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[], # Add any dependencies here
    test_suite='nose.collector', # For nosetests
)