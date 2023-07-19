import matplotlib.pyplot as plt
import numpy as np

# Data 

years = np.arange(2023, 2026)
total_market = np.array([50000, 51000, 53000, 54000, 55000, 5000])
kisoboka_market = np.array([3000, 4500, 6000, 7500, 9000, 10000])

# Plot

plt.plot(years, total_market, label='Total Market')
plt.plot(years, kisoboka_market, label ='Kisoboka Africa Market')
plt.xlabel('Year')
plt.ylabel('Number of Households in Lwengo')
plt.title('Kisoboka Africa Target Market and Market Share')
plt.legend()
plt.show()


