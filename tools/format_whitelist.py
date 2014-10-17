#!/usr/bin/env python2
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file', help='The whitelist file to format.')
args = parser.parse_args()

with open(args.file, 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.rstrip('\n')
    f.seek(0)
    f.write('\n'.join(sorted(lines)) + '\n')
