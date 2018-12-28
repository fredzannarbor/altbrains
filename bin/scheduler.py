# -*- coding: utf-8 -*-
"""


"""

import logging
import argparse
import schedule



logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("--infile", help = "seed file", default = 'test')
parser.add_argument("--lang", help="wiki language bigram", default = 'en')
parser.add_argument("--request_type", help="request type", default = 'sum')
parser.add_argument("--outfile", help = "path to outfile", default = 'outfile')
parser.add_argument("--summary", help = "true or false", action = "store_false")
parser.add_argument("--logging", help = "true or false", action = "store_true")
parser.add_argument("--mediawiki_api_url", help = "true or false", default = 'en.wikipedia.org')
parser.add_argument("--url_prefix", help = "default wiki ssl value is https", default = 'https')
parser.add_argument("--wikipath", help = "mediawiki default is /w/api.php", default = '/w/')
parser.add_argument("--cats_file", help = "path to outfile", default = 'cats')
parser.add_argument("--extlinks_file", help = "path to outfile", default = 'extlinks')

args = parser.parse_args()

input_file = args.infile
output_file = args.outfile
cats_file = args.cats_file
extlinks_file = args.extlinks_file
lang = args.lang
summary = args.summary
logging = args.logging

print('hello wordl')

