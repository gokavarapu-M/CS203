import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# data
# 1 for heads (H), 0 for tails (T)

data = np.array([1, 1, 1, 0, 0, 0, 1, 1, 1, 0])  
trials = len(data)
heads = np.sum(data)
tails = trials - heads

# Prior hyperparameters
priors = [(2, 5), (5, 2), (1, 1), (2, 2)]

plt.figure(figsize=(12, 8))

idx = 1
case_no = 1;

for prior in priors:
  a,b = prior
  x = np.linspace(0,1,1000)

  beta_graph = beta.pdf(x, a, b)               # Prior Beta function

  plt.subplot(4,2,idx)
  plt.plot(x, beta_graph, label=f'Prior Beta({a},{b})')
  plt.title(f'Case: {case_no} Prior')
  plt.xlabel('Bias')
  plt.ylabel("Probability Denisty")
  plt.legend()

  a_post = a + heads
  b_post = b + tails

  mle = heads/trials                           # Maximum Likelihood Estimate
  map = (a_post - 1)/(a_post+b_post - 2)       # Maximum a Posteriori

  beta_post = beta.pdf(x,a_post,b_post)        # Posterior Beta function
  
  plt.subplot(4,2,idx+1)
  plt.plot(x,beta_post, label = f'Posterior Beta({a_post},{b_post})')
  plt.axvline(mle, color='r', linestyle='--', label=f'MLE: {mle:.2f}')
  plt.axvline(map, color='g', linestyle='--', label=f'MAP: {map:.2f}')
  plt.title(f'Case: {case_no} Posterior')
  plt.xlabel("Bias")
  plt.ylabel('Probability Density')
  plt.legend()

  case_no = case_no + 1
  idx = idx + 2

plt.tight_layout()
plt.show()
