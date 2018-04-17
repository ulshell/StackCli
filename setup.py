from setuptools import setup
#-e,--editable <path/url>
#Install a project in editable mode (i.e.  setuptools "develop mode") from a local project path.
setup(
    name="stack",
    version='1.0',
    py_modules=['mystack'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        stack=mystack:cli
    ''',
)
