from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'django-clear-cache',
    version = '0.3',
    packages = (
        'clear_cache',
        'clear_cache.management',
        'clear_cache.management.commands'
    ),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['Django>=1.0'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/django-clear-cache',
    keywords = 'django cache management memcached clear',
    description = 'A simple Django management command which clears your cache.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
