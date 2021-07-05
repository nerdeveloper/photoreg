from setuptools import setup

setup(
    name='photoreg',
    version='0.1.0',
    py_modules=['photoreg'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        photoreg=photoreg:cli
    ''',
)
