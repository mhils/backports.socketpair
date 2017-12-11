from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='backports.socketpair',
    version='3.5.0.3',
    description='Python 2 support for socket.socketpair() on Windows',
    long_description=long_description,
    url='https://github.com/mhils/backports.socketpair',
    author='Maximilian Hils',
    author_email='socketpair@maximilianhils.com',
    license='Python Software Foundation License',
    keywords='socket socketpair backport',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Python Software Foundation License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages('.'),
    namespace_packages=['backports'],
    include_package_data=True,
)
