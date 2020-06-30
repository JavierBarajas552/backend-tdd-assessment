#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "???"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', action='store_true', help='lowercase mod')
    parser.add_argument('-t', action='store_true', help='Titlecase mod')
    parser.add_argument('-u', action='store_true', help='uppercase mod')
    parser.add_argument('text', help='text to echo')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)
    output = args.text
    if args.l:
        output = output.lower()
    if args.u:
        output = output.upper()
    if args.t:
        output = output.title()
    print(output)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
