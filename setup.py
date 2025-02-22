from setuptools import setup, find_packages

# load readme
with open('readme.md', 'r') as file:
    readme = file.read()

setup(
    name='sriracha',
    version='0.1.1',
    description='MVC Web Framework',

    author='pc',
    author_email='crunch@disroot.org',

    long_description=readme,
    long_description_content_type='text/markdown',

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
