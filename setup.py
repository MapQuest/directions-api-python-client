try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

def isCorrectPYVersion():
    sys_py_version = sys.version_info
    return sys_py_version <= (2,7)

if not isCorrectPyVersion():
    print >> sys.stderr, "Project requires CPython v. 2.7"
    sys.exit(1)

requirements = [
        'requests<=2.10.0'
]


setup(
        name='mapquest',
        version='1.0.0a',
        description='MapQuest Directions API',
        url='',
        author='MapQuest',
        author_email='developer@mapquest.com',
        license='MIT',
        classifiers=[
            'Development Status :: 1 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Maps, Directions',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7'
            ],
        keywords='maps directions routing'
)


