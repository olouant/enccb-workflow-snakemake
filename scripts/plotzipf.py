import os
import sys
import math

import matplotlib.pyplot as plt

def read_data(input):
  data = {}
  with open(input, 'r') as infile:
    for line in infile:
      fields = line.split()
      key = fields[0]
      val = fields[1]
      
      data[key] = val
  
  return data
  
def plot_zipf(input_freqs, input_fit, output):
  freq_data = read_data(input_freqs)
  fit_data = read_data(input_fit)
    
  alpha = float(fit_data['alpha'])
  c = float(fit_data['c'])
  total_words = int(fit_data['total_words'])
  distinct_words = int(fit_data['distinct_words'])
  title =  os.path.splitext(os.path.basename(input_freqs))[0]
  
  ranks = [i for i in range(1, distinct_words + 1)]
  fitted = [total_words / c * rank ** (-alpha) for rank in ranks]
  freqs = [int(freq) for freq in freq_data.values()]
  
  plt.figure(figsize=(6, 6))
  plt.loglog(ranks, freqs)
  plt.loglog(ranks, fitted)
  plt.title(title)
  plt.xlabel('Rank of word')
  plt.ylabel('Number of occurences')
  plt.legend(['Empirical', 'Fit'])

  plt.savefig(output)

if __name__ == '__main__':
  input_freqs = sys.argv[1]
  input_fit = sys.argv[2]
  output = sys.argv[3]
  
  plot_zipf(input_freqs, input_fit, output)