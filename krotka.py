# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# Data
x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x,y)

# Multivariate Normal
mu_x = np.mean(x)
sigma_x = np.std(x)
mu_y = np.mean(y)
sigma_y = np.std(y)
rv = multivariate_normal([mu_x, mu_y], [[sigma_x, 0], [0, sigma_y]])

# Probability Density
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y
pd = rv.pdf(pos)

# Plot
fig = plt.figure()
ax = fig.gca()
plt.contourf(X,Y,pd)
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.set_zlabel('Probability Density')
plt.title("Multivariate Normal Distribution")
plt.show()
