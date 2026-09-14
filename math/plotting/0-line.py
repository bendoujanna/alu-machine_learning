#!/usr/bin/env python3
"""Plot y as a solid red line graph with x ranging from 0 to 10."""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(range(11), y, 'r-')
plt.xlim(0, 10)
plt.show()