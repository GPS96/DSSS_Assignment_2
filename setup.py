from setuptools import setup, find_packages

setup(
    name='DSSS_Assignment_2',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        'python>=3.7.0',
        'numpy>=1.23.5',
        'pandas>=1.5.3',
        'openpyxl>=3.0.10'
    ],
    entry_points={
        'console_scripts': [
            'dsss_assignment_2 = dsss_assignment_2.module:main_function',
        ],
    },
    # Other project metadata
    author='Gyan Prakash Sahoo',
    description='Hands on experience with creating and managing repository on GitHub',
    url='https://github.com/GPS96/DSSS_Assignment_2',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)