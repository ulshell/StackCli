from setuptools import setup

setup(
    name="stack",
    version='0.1',
    py_modules=['mystack'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        stack=mystack:cli
    ''',
)
