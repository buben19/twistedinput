from __future__ import unicode_literals
from setuptools import setup, find_packages
import os



def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

required = ['Twisted', 'zope.interface']
setup(
    name                = 'twistedinput',
    version             = '0.0.1',
    author              = 'Ivo Slanina',
    author_email        = 'ivo.slanina@gmail.com',
    description         = 'Reading input devices with Twisted.',
    license             = 'Unlicence',
    keywords            = 'twisted gamepad input joystick mouse',
    url                 = 'https://github.com/buben19/twistedinput',
    long_description    = read('README.md'),
    classifiers         = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware :: Hardware Drivers'],
    install_requires    = required,
    packages            = find_packages())
