from setuptools import setup, find_packages

setup(
    name='DSSS_Assignment_2',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        'numpy>=1.26.1',
        'pandas>=2.1.2',
    ],
    entry_points={
        'console_scripts': [
            'dsss_assignment_2 = dsss_assignment_2.module:math_quiz',
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