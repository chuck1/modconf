
import re
from setuptools import setup

with open('modconf/__init__.py') as f:
    version = re.findall("^__version__ = '(.*)'", f.read())[0]

setup(name='modconf',
        version=version,
        description='pattern for using python modules as configuration files',
        url='http://github.com/chuck1/modconf',
        author='Charles Rymal',
        author_email='charlesrymal@gmail.com',
        license='MIT',
        packages=(
            'modconf',
            'modconf.tests'),
        package_data={'': ['*.txt']},
        zip_safe=False,
        )

