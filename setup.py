from setuptools import setup, find_packages

setup(
    name='faster',
    version='0.1.0',
    description='Football data analysis',
    author='Steven Taylor',
    url='https://github.com/tayl0r89/faster',
    packages=find_packages(exclude=('tests', 'docs'))
)