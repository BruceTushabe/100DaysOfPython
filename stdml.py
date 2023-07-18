# Lets deal with standard deviation 

import numpy as np
import matplotlib.pyplot as plt
speed = [86,87,88,86,87,85,86]


x = np.std(speed)

y = np.var(speed)

# Creating random datasets

x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x,100)
plt.show()

print(x)






