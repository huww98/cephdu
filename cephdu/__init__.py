#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path
from typing import List

UNITS = ['', 'K', 'M', 'G', 'T', 'P']
STEP = 1024

def to_human_readable(size: int):
    def f():
        return f'{size:.1f}{u}' if u else str(size)

    for u in UNITS:
        if size < STEP:
            return f()
        size /= STEP

    return f()


def du_recursive(path: Path, human_readable=False, depth=float('inf')):
    if depth < 0:
        return 0

    try:
        if path.is_dir() and not path.is_symlink():
            for c in path.iterdir():
                du_recursive(c, human_readable, depth - 1)
            p = str(path) + os.path.sep
            try:
                size = int(os.getxattr(path, 'ceph.dir.rbytes'))
            except OSError as ex:
                raise RuntimeError('Maybe not an directory from CephFS?') from ex
        else:
            p = str(path)
            size = path.lstat().st_size

        size_str = to_human_readable(size) if human_readable else str(size)
        print(f'{size_str}\t{p}')
        return size
    except PermissionError as ex:
        print(ex, file=sys.stderr)
        return 0

def du(path: List[Path], human_readable=False, total=False, max_depth=float('inf')):
    total_size = 0
    for p in path:
        total_size += du_recursive(p, human_readable, max_depth)

    if total:
        if human_readable:
            total_size = to_human_readable(total_size)
        print(f'{total_size}\ttotal')


def main():
    parser = argparse.ArgumentParser(
        description='A "du" like utility to estimate file space usage that utilizes CephFS extended file attribute "ceph.dir.rbytes".',
        conflict_handler='resolve'
    )
    parser.add_argument('path', type=Path, default=[Path('.')], nargs='*')
    parser.add_argument('-h', '--human-readable', action='store_true',
                        help='print sizes in human readable format (e.g., 1K 234M 2G)')
    parser.add_argument('-c', '--total', action='store_true',
                        help='produce a grand total')
    parser.add_argument('-d', '--max-depth', type=int, default=float('inf'), metavar='N',
                        help='print the total for a directory or file only if it is N or fewer levels below the command line argument')
    args = parser.parse_args()
    du(**vars(args))
