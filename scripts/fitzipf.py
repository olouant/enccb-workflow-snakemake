import sys
import numpy as np

from scipy.optimize import minimize_scalar

def read_data(input):
  count = []
  with open(input, 'r') as infile:
    for line in infile:
      fields = line.split()
      count.append(int(fields[1]))

  return np.array(count)

def zipf_fit(word_counts):
  mle = minimize_scalar(_nlog_likelihood, bracket=(1 + 1e-10, 4), args=word_counts)
  beta = mle.x
  alpha = 1 / (beta - 1)
  
  # Estimate the constant C so that this distribution integrates to 1.
  # https://en.wikipedia.org/wiki/Zipf%27s_law
  c = ((np.arange(len(word_counts)) + 1) ** (-alpha)).sum()

  return alpha, c

def _nlog_likelihood(beta, counts):
  """
  Log-likelihood function.
  """
  likelihood = -np.sum(np.log((1 / counts) ** (beta - 1) - (1 / (counts + 1)) ** (beta - 1)))
  
  return likelihood

if __name__ == '__main__':
  input = sys.argv[1]
  output = sys.argv[2]
  
  count = read_data(input)
  alpha, c = zipf_fit(count)
  
  out = {
    'total_words': count.sum(), 
    'distinct_words': len(count), 
    'alpha': alpha, 
    'c': c
  }
  
  with open(output, 'w') as outfile:
    for key, val in out.items():
      outfile.write('{:s} {:s}\n'.format(key, str(val)))