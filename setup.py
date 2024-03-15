from setuptools import setup, find_packages

setup(
    name='oliseh-efris-tools',
    version='0.1.0',
    author='Oliseh Genesis',
    author_email='innovationsug@yahoo.com',
    description='Tools for interacting with the URA eFRIS API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/olisehgenesis/oliseh_efris_tools',
    packages=find_packages(),
    install_requires=[
        'requests',  # Example dependency
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
)
