from setuptools import setup, find_packages

setup(
    name='wifi-wordlist-generator',
    version='1.0.0',
    packages=find_packages(),
    py_modules=['cli'],
    install_requires=[
        'click',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'wifi-wordlist-generator = cli:cli',
        ],
    },
)
