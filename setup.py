"""Setup script for 'Vindtunnel Machine Learning' program."""

import os
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

version = '0.0.1'

setup(name='vindtunnel_ml',
      version=version,
      description="Creates reports to support the management team analysis.",
      lon_gdescription=README,
      long_description_content_type="text/markdown",
      url="https://github.com/flaviassantos/vindtunnel_ml",
      author="Flávia Santos",
      author_email="ssantosflavia@hotmail.com",
      classifiers=[
          "Programming Language :: Python :: 3"
      ],
      packages=['vindtunnel_ml'],
      python_requires='>=3.7',
      install_requires=[
      ],
      entry_points={
          'console_scripts': [
              'vindtunnel_ml = vindtunnel_ml.__main__:main'
          ]  # ['name_of_executable = module.with:function_to_execute']
      },
      )