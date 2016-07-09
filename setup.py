from setuptools import setup
from os import path

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

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        ],
      packages=['contacts'],
      entry_points = {
          'console_scripts': ['contact-search=contacts.command_line:main'],
      },
      include_package_dirs=True,
      zip_safe=False
)
