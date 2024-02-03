from setuptools import setup, find_packages

setup(
    name='hello flask',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_restful'
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'run_flask_app = hello_flask:app.run',
        ],
    },
)