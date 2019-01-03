# -*- coding: utf-8 -*-
"""

Fred Zimmerman
wfzimmerman#gmail.com

loops over a file, fetches URLs line by line, and converts them to readable tect

"""

import logging
import argparse
from pattern.web import URL, plaintext, decode_utf8

logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("--infile", help = "urls", default = 'urls/test')
parser.add_argument("--lang", help="wiki language bigram", default = 'en')
parser.add_argument("--outfile", help = "path to outfile", default = 'outfile')
parser.add_argument("--logging", help = "logging", default = 'WARNING')
args = parser.parse_args()

input_file = args.infile
output_file = args.outfile

lang = args.lang

logging = args.logging


file1 = open(input_file, 'r').read().splitlines()
file2 = open(output_file, 'w')

for line in file1:
    try:
        print('seed is ' + line)
        s = URL(line).download()
        #print(s) 
        d = decode_utf8(s)
        s = plaintext(d, keep={'h1':[], 'h2':[], 'strong':[], 'li' 'a':['href']}, )
        #print('not s')
        print(s)
    except:
        continue
    file2.write('\n')
    #print(text)
    file2.write('\n')
    file2.write('# ' )
    file2.write(s)
    file2.write('\n')

file2.close
