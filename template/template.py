#! /usr/bin/env python3

'''
Advent of Code 2023 - Template

'''

import sys
import argparse
import inspect
import re

def parse_line(line, part = 2, verbose = False):
    numbers = map(int, re.findall(r'(\d+)', line))
    return sum(numbers)*part

def parse_args():
    parser = argparse.ArgumentParser(usage= '''Usage:
        cat data.txt | template.py [-v] [--part 1]
        python3 -m template.py --file data.txt [-v] [--part 1]''')
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

    values = [parse_line(line, args.part, args.verbose) for line in lines]
    total = sum(values)

    frame = inspect.currentframe().f_back
    if frame.f_code.co_nlocals > 0:
        return total
    else:
        print(f'Score: {total}')

if __name__ == '__main__':
    args = parse_args()
    main(args)

