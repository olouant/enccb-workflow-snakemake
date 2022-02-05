#!/usr/bin/env python

import sys

from operator import itemgetter

def read_input(input, data):
  with open(input, 'r') as infile:
    for line in infile:
      fields = line.split()
      word = fields[0]
      count = int(fields[1])
            
      if word in data.keys():
        data[word] += count
      else:
        data[word] = count

if __name__ == "__main__":  
  data = {}
  for input in snakemake.input:
    read_input(input, data)
    
  sorted_data = reversed(sorted(data.items(), key = itemgetter(1)))

  with open(snakemake.output[0],'w') as outfile:
    for key, value in sorted_data:
      outfile.write('{:s} {:d}\n'.format(key, value))