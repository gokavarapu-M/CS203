import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv  # inverse of error function
from scipy.stats import norm  #normal cdf


#Inputs for mu and sigma
mu = float(input("Enter the value of 'mu': "))
sigma = float(input("Enter the value of 'sigma': "))

while sigma < 0:
   print("Error: 'sigma' must be greater than 0.")
   sigma = float(input("Enter the value of 'sigma': "))

# Inputs for the interval [a, b]
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

# Loop until a valid value for 'b' is entered
while b <= a:
    print("Error: 'b' must be greater than 'a'.")
    b = float(input("Enter the value of 'b': "))

# Generate 100,000 random numbers from a uniform distribution
uniform_rv = np.random.uniform(norm.cdf((a-mu)/sigma),norm.cdf((b-mu)/sigma),1000000)

# Inverse CDF transformation for Standard Normal Distribution
gaussian_rv = mu + sigma*np.sqrt(2) * erfinv(2 * uniform_rv - 1)

# Taking the samples within [a, b]
gaussian_rv = [i for i in gaussian_rv if i >= a and i <= b]

# Calculate the heights of the histogram bins
counts, bins = np.histogram(gaussian_rv, bins=1000, range=(a, b), density=True)

# Calculate the current total area under the histogram
total_area = np.sum(counts * np.diff(bins))

# Calculate the desired area under the histogram
desired_area = norm.cdf((b-mu)/sigma) - norm.cdf((a-mu)/sigma)

# Calculate the scaling factor to achieve a total area of 0.75
scaling_factor = desired_area / total_area

# Scale the heights of the histogram bins by the scaling factor
scaled_counts = counts * scaling_factor

# Plot the scaled histogram
plt.bar(bins[:-1], scaled_counts, width=np.diff(bins), alpha=0.6, color='b')

# Plot the theoretical Standard Normal Distribution curve for comparison
x = np.linspace(a, b, 1000)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
plt.plot(x, y, color='r')

plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Scaled Histogram of Normal Distribution Samples in the Interval [' + str(a) + ', ' + str(b) + ']')
plt.legend(['Theoretical Normal', 'Scaled Histogram'])
plt.grid(True)
# plt.ylim(norm.cdf(b), norm.cdf(a))
plt.show()
