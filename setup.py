from setuptools import setup

setup(
    name='usertohash',
    version='0.1',
    py_modules=['usertohash'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        usertohash=usertohash:makeitso
    ''',
)