#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='cephdu',
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
