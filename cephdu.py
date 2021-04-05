#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path

UNITS = ['', 'K', 'M', 'G', 'T', 'P']
STEP = 1024

def to_human_readable(size: int):
    def f():
        if u:
            return f'{size:.1f}{u}'
        return str(size)

    for u in UNITS:
        if size < STEP:
            return f()
        size /= STEP

    return f()


def du(path: Path, human_readable=False):
    for c in path.iterdir():
        try:
            if c.is_dir() and not c.is_symlink():
                p = str(c) + os.path.sep
                size = int(os.getxattr(c, 'ceph.dir.rbytes'))
            else:
                p = str(c)
                size = c.lstat().st_size

            if human_readable:
                size = to_human_readable(size)
            print(f'{size}\t{p}')
        except PermissionError as ex:
            print(ex, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='A "du" like utility to estimate file space usage that utilizes CephFS extended file attribute "ceph.dir.rbytes".',
        conflict_handler='resolve'
    )
    parser.add_argument('path', type=Path, default=Path('.'))
    parser.add_argument('-h', '--human-readable', action='store_true',
                        help='print sizes in human readable format (e.g., 1K 234M 2G)')
    args = parser.parse_args()
    du(**vars(args))


if __name__ == '__main__':
    main()
