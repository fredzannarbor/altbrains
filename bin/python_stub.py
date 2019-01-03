# -*- coding: utf-8 -*-
"""

Fred Zimmerman
wfzimmerman#gmail.com



"""

import logging
import argparse
import mwclient


logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("--infile", help = "seed file", default = 'test')
parser.add_argument("--lang", help="wiki language bigram", default = 'en')
parser.add_argument("--request_type", help="request type", default = 'sum')
parser.add_argument("--outfile", help = "path to outfile", default = 'outfile')

args = parser.parse_args()

input_file = args.infile
output_file = args.outfile

lang = args.lang

logging = args.logging



file1 = open(input_file, 'r').read().splitlines()
file2 = open(output_file, 'w')

#file4 = open(extlinks_file, 'a+')
for line in file1:
    try:
        print('seed is ' + line)
        
    except:
        mwclient.errors.InvalidPageTitle
        continue
    file2.write('\n')
    #print(text)
    file2.write('\n')
    file2.write('# ' )
    file2.write(line)
    file2.write('\n')
    file2.write(text)
    

file2.close
