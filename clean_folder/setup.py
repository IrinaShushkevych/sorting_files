from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(name='clean_folder',
      version='1.0',
      description='Code for sorting files in a directory',
      author='Irina Shushkevych',
      entry_points={
            'console_scripts':['clean_folder=clean_folder.sorting_files:main']
      },
      packages=find_packages()
      )