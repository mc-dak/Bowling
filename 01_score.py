# -*- coding: utf-8 -*-

import argparse

from bowling import get_score

parser = argparse.ArgumentParser(description='Script for counting of scores')

if __name__ == "__main__":
    parser.add_argument('--result', action="store", dest="result", required=True)
    parser.add_argument('--type', action="store", dest="type", required=True)

args = parser.parse_args()

get_score(args.result, args.type)
