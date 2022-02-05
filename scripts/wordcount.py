#!/usr/bin/env python

import re
import sys

from operator import itemgetter

def word_count(input):
    """
    Returns a dictionary with the frequency of words
    in a text file
    """
    frequency = {}

    infile = open(input, 'r')
    content = infile.read().lower()
    infile.close()

    words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', content)
    for word in words:
        count = frequency.get(word,0)
        frequency[word] = count + 1

    return reversed(sorted(frequency.items(), key = itemgetter(1)))


if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]

    word_freq = word_count(input)

    with open(output,'w') as outfile:
        for key, value in word_freq:
            outfile.write('%s %d\n' % (key, value))
