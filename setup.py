import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

NAME = 'Server Application'
DESCRIPTION = ''
URL = 'https://github.com/OlenaHolub/server_app/'
EMAIL = 'else.golub@gmail.com'
AUTHOR = 'Olena Holub'

with codecs.open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name=NAME,
    version='',
    packages=find_packages(),
    url=URL,
    license='MIT',
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False
)
