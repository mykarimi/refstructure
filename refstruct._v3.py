#!/bin/env/python3

import sys
import os
import re
import itertools
from nltk import sent_tokenize


with open(sys.argv[1], 'r') as section:
    text = section.read().replace('\n', '')
    note_references = re.findall('(<note ref>.*?</note ref>)', text)
    sentences = []
    for reference in note_references:
    	text = text.replace(reference, '')
    	sentences = sent_tokenize(text)

for sentence in sentences:
	print(sentence)

for reference in note_references:
	print(reference)
