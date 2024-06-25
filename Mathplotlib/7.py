import matplotlib.pyplot as plt
import random as rnd
x = rnd.randint(10,10000)

plt.hist(x, bins=10)
plt.show()