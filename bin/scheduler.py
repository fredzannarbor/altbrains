# -*- coding: utf-8 -*-
"""


"""

import logging
import argparse
import schedule
import time
import subprocess


logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("--infile", help = "seed file", default = 'test')
parser.add_argument("--logging", help = "true or false", action = "store_true")

args = parser.parse_args()

input_file = args.infile
output_file = args.outfile
cats_file = args.cats_file
extlinks_file = args.extlinks_file
lang = args.lang
summary = args.summary
logging = args.logging

print('hello wordl')

