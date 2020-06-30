#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "???"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='text to echo')
    parser.add_argument('-l', help='lowercase mod')
    parser.add_argument('-t', help='Titlecase mod')
    parser.add_argument('-u', help='uppercase mod')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)
    print(args.text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
