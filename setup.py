from setuptools import setup
from os import path
import tarfile

DIR_NAME = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(DIR_NAME, 'README.rst')) as f:
    long_description = f.read()

setup(name='Contacts',
      version='1.0',
      description='Search and store contacts',
      long_description=long_description,
      url='http://github.com/tirkarthi/helpshift-search-contacts',
      author='Xtreak',
      author_email='tir.karthi@gmail.com',
      license='MIT',

      classifiers=[
        'Development Status :: 5 - Stable',

        'Intended Audience :: Authors Students',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        ],
      scripts = ['scripts/contacts'],
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=['contacts'],
      zip_safe=False)
