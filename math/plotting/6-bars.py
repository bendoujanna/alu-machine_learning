#!/usr/bin/env python3
"""Plot a stacked bar graph of fruit quantities per person."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
x = np.arange(len(people))
width = 0.5

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

plt.bar(x, apples, width=width, color='red', label='apples')
plt.bar(x, bananas, width=width, color='yellow', label='bananas',
        bottom=apples)
plt.bar(x, oranges, width=width, color='#ff8000', label='oranges',
        bottom=apples + bananas)
plt.bar(x, peaches, width=width, color='#ffe5b4', label='peaches',
        bottom=apples + bananas + oranges)

plt.xticks(x, people)
plt.ylabel('Quantity of Fruit')
plt.yticks(range(0, 81, 10))
plt.ylim(0, 80)
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()