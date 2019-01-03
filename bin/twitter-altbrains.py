#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:04:18 2019

altbrains twitter module loops over a file of search phrases
and saves the result to a specified text file.


@author: fzimmerman
"""

from pattern.web import Twitter, plaintext
import logging

import argparse

logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("--infile", help = "seed file", default = 'test')
parser.add_argument("--lang", help="wiki language bigram", default = 'en')
parser.add_argument("--outfile", help = "path to outfile", default = 'outfile')
parser.add_argument("--logging", help = "true or false", action = "store_true")


args = parser.parse_args()

input_file = args.infile
output_file = args.outfile
lang = args.lang
logging = args.logging

twitter = Twitter(language=lang) 

print(input_file)

file1 = open(input_file, 'r').read().splitlines()
file2 = open(output_file, 'w')
for line in file1:
    print('search phrase is ' + line)
    for tweet in twitter.search(line, cached=False):
        print(plaintext(tweet.text))
        file2.write('\n')
        file2.write('\n')
        file2.write('# ' )
        file2.write(plaintext(tweet.text))
file2.close()
