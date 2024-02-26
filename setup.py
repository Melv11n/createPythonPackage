from setuptools import setup, find_packages
setup(
    name = 'pythonPackage00',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'Example of a Python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/Melv11n/pythonPackage',
    author = 'Melvin Baraka',
    email = 'melvinbaraka11@gmail.com'
)