#!/usr/bin/env python
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='cephdu',
    description='A "du" like utility to estimate file space usage on CephFS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/huww98/cephdu',
    maintainer='Weiwen Hu',
    maintainer_email='huww98@outlook.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cephdu=cephdu:main',
        ],
    },
    setup_requires=[
        'setuptools',
        'setuptools_scm',
    ],
    keywords=['ceph', 'cephfs', 'du'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Monitoring',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    use_scm_version=True,
)
