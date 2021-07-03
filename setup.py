from setuptools import setup, find_packages

setup(
    name='sriracha',
    version='0.1',
    description='MVC Web Framework',

    author='pc',
    author_email='crunch@disroot.org',

    packages=find_packages(),

    install_requires=['python-liquid', 'click', 'GitPython'],

    entry_points={
        'console_scripts': [
            'sri=sri:main'
        ]
    },

    license='GPL',
    license_file='LICENSE'
)
