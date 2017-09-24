from setuptools import setup

setup(name='sample-data-generator',
      version='0.1',
      description='Generate sample for machine learning',
      url='http://github.com/anthonymak/datascience/sample-data-generator',
      author='Anthony Mak',
      author_email='anthonycwmak@gmail.com',
      packages=['features', 'models'],
      install_requires=[
          'numpy',
      ])