from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='spreadsheet2shortlinks',
    version='0.1',
    # Look for anki package in anki/anki
    package_dir={'civictechto_scripts': 'civictechto_scripts'},
    packages=find_packages() + find_packages('civictechto_scripts', include=['*']),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    # TODO: Fetch meetup-api from custom fork.
    entry_points={
        'console_scripts': [
            'spreadsheet2shortlinks=spreadsheet2shortlinks.cli:gsheet2rebrandly',
        ],
    }
)
