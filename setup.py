"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import os
import shutil
from setuptools import setup, find_packages
from release import __version__, __author__
# To use a consistent encoding
# from codecs import open

# here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()
if not os.path.exists('/apps/conf/linkage'):
    os.makedirs('/apps/conf/linkage')
if os.path.exists('/apps/conf/linkage/instance'):
    shutil.rmtree('/apps/conf/linkage/instance')
shutil.copytree('instance', '/apps/conf/linkage/instance')

setup(
    name='linkage',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='A gateway that connects to multiple systems',
    # long_description=long_description,

    # The project's main homepage.
    url='http://cloudlab051/promise/linkage.git',

    # Author details
    author=__author__,
    author_email='freedom_whm@163.com',

    # Choose your license
    license='GNU',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    # keywords='CLI NETWORK AUTO-OPERATION',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # package_dir={'': 'lib'},
    packages=find_packages(exclude=["tests.*", "tests", "instance", "docs", "protocol"]),
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
#    install_requires=[
#        'paramiko==1.16.0',
#        'mock==2.0.0',
#        'flake8==2.4.1',
#        'appdirs==1.4.3',
#        'ecdsa==0.13',
#        'funcsigs==1.0.2',
#        'mccabe==0.3.1',
#        'packaging==16.8',
#        'pbr==3.0.0',
#        'pep8==1.7.0',
#        'pycrypto==2.6.1',
#        'pyflakes==0.8.1',
#        'pyparsing==2.2.0',
#        'six==1.10.0'
#    ],
#    install_requires=[
#        'paramiko==1.16.0',
#        'mock==2.0.0',
#        'flake8==2.4.1',
#        'appdirs==1.4.3',
#        'ecdsa==0.13',
#        'funcsigs==1.0.2',
#        'mccabe==0.3.1',
#        'packaging==16.8',
#        'pbr==3.0.0',
#        'pep8==1.7.0',
#        'pycrypto==2.6.1',
#        'pyflakes==0.8.1',
#        'pyparsing==2.2.0',
#        'six==1.10.0'
#    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #    '': [],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
