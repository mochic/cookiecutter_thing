from glob import glob
from os import path
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), 'r') as rstream:
    readme = rstream.read()


setup(
    name='{{cookiecutter.package_name}}',
    version='{{cookiecutter.version}}',
    license='{{cookiecutter.license}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    long_description=readme,
    description='{{cookiecutter.description}}',
    packages=find_packages('src'),
    package_dir={'': 'src', },
    py_modules=[
        path.splitext(path.basename(path))[0]
        for path in glob('src/*.py')
    ],
    include_package_data=True,
    zip_safe=False,
)
