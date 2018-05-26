try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test Driven Development in Python',
    'author': 'Ross Kraybill',
    'url': 'url',
    'download_url': 'download_url',
    'version': '0.1',
    'install_requires': ['nose'],
    'package': ['tdd'],
    'scripts': ['./bin/script.py'],
    'name': 'tdd'
}

setup(**config)


