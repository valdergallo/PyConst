#!/usr/bin/env python
import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import pyconst

tests_requires = [
    'pytest==3.0.3',
    'pytest-cov==2.4.0',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '--cov=pyconst', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except:
        return '''PyConst one simple way to organize the constants'''


setup(name='pyconst',
      url='https://github.com/valdergallo/pyconst',
      download_url='https://github.com/valdergallo/pyconst/tarball/%s/' % pyconst.get_version(),
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords=['constants', 'django', 'data', 'control'],
      description='PyConst one simple way to organize the constants',
      license='GPL-3.0',
      long_description=readme(),
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      include_package_data=True,
      version=pyconst.get_version(),
      tests_require=tests_requires,
      cmdclass={'test': PyTest},
      packages=['pyconst'],
      zip_safe=False,
      platforms='any',
)
