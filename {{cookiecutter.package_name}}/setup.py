from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup


setup(
    name='{{cookiecutter.package_name}}',
    version='{{cookiecutter.version}}',
    license='{{cookiecutter.license}}',
    description='{{cookiecutter.description}}',
    packages=find_packages('src'),
    package_dir={'': 'src', },
    py_modules=[
        splitext(basename(path))[0]
        for path in glob('src/*.py')
    ],
    include_package_data=True,
    zip_safe=False,
)