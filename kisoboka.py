import matplotlib.pyplot as plt
import numpy as np

# Data 

years = np.arange(2020, 2026)
total_market = np.array([50000, 52000, 54000, 56000, 58000, 60000])
kisoboka_market = np.array([10000, 12000, 14000, 16000, 18000, 20000])

# Plot

plt.plot(years, total_market, label='Total Market')
plt.plot(years, kisoboka_market, label ='Kisoboka Market')
plt.xlabel('Year')
plt.ylabel('Number of Households')
plt.title('Kisoboka Africa Target Market and Market Share')
plt.legend()
plt.show()


