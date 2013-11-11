"""
Flask-PageDown
--------------

Implementation of StackOverflow's "PageDown" markdown editor for Flask-WTF.
"""
from setuptools import setup


setup(
    name='Flask-PageDown',
    version='0.1.2',
    url='http://github.com/miguelgrinberg/flask-pagedown/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description='Implementation of StackOverflow\'s "PageDown" markdown editor for Flask-WTF.',
    long_description=__doc__,
    packages=['flask_pagedown'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'WTForms'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
