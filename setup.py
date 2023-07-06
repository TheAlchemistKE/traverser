from setuptools import setup, find_packages

setup(
    name='traverser',
    version='1.0.0',
    packages=find_packages(),
    entry_points={'console_scripts': ['traverser=app:main']},
    license='MIT',
    author='Kelyn Njeri',
    author_email='kelyn.njeri@gmail.com',
)