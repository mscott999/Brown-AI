import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = (30 * np.random.rand(n))**2

plt.scatter(x, y, s = area, c = colors, alpha = 0.5,)
plt.show()
