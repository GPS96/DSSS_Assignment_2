from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    py_modules= ['math_quiz'],
    install_requires=[
        # List your project dependencies here
        'numpy>=1.26.1',
        'pandas>=2.1.2',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:main',
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