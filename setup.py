from setuptools import setup

setup(
    name='flaskr',
    version='1.0.0',
    url='https://flask.palletsprojects.com/tutorial/',
    license='BSD-3-Clause',
    author='Pallets',
    author_email='contact@palletsprojects.com',
    description='The basic blog app built in the Flask tutorial.',
    install_requires=['flask', 'gunicorn']
)
