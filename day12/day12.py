#! /usr/bin/env python3

'''
Advent of Code 2023 - Day12

'''

import sys
import argparse
import inspect
import numpy as np
import re
import itertools

def check_line(line, groups):
    pattern = match_pattern(groups)
    return pattern.match(line) is not None

def match_pattern(groups):
    pattern = '[^#]*'
    for g in groups:
        pattern += (f'(#{{{g}}})(?!#).*')
    return re.compile(pattern)

def parse_line(line, part, verbose = False):

    groups = list(map(int, re.findall(r'(\d+)', line)))
    record = np.array(list(re.match(r'[?.#]+', line).group(0)))

    if part == 2:
        groups = groups*5
        record = np.concatenate([record]*5)

    pattern = match_pattern(groups)

    unknown = np.where(record == '?')[0]
    damaged = np.where(record == '#')[0]
    missing = sum(groups) - len(damaged)
    # missing_damaged = sum(groups) - len(damaged)
    # missing_operating = len(unknown) - missing_damaged
    # if missing_damaged < missing_operating:
    #     missing = missing_damaged
    #     stuff = '#'
    # else:
    #     missing = missing_operating
    #     stuff = '.'

    if verbose:
        print(f'{line}: {missing} missing #')

    test = record.copy()
    if missing == 0:
        nopts = 1
    else:
        nopts = 0
        for idx in itertools.combinations(unknown, missing):
            test[unknown] = '.'
            test[np.array(idx)] = '#'
            modline = ''.join(test)
            if pattern.match(modline) is not None:
                nopts += 1
                if verbose:
                    print(''.join(test) + ' works')

    return nopts

def parse_args():
    parser = argparse.ArgumentParser(usage= '''Usage:
        cat data.txt | day12.py [-v] [--part 1]
        python3 -m day12.py --file data.txt [-v] [--part 1]''')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--part', type=int, default=2, help='Specify the part number')
    parser.add_argument('--file', type=str, help='Specify input file')
    return parser.parse_args()

def main(args):

    if args.file:
        with open(args.file) as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    total = 0
    for i, line in enumerate(lines):
        values = parse_line(line, args.part, args.verbose)
        total += values

        progress = (i + 1) / len(lines) * 100
        print(f'Progress: {progress:.2f}%')

    frame = inspect.currentframe().f_back
    if frame.f_code.co_nlocals > 0:
        return total
    else:
        print(f'Score: {total}')

if __name__ == '__main__':
    args = parse_args()
    main(args)

