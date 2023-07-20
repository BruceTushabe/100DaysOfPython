import matplotlib.pyplot as plt
import numpy as np

years = range(2020, 2026)
oranges = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
matooke = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(years, oranges, label='Oranges', color= "orange")
plt.bar(years, matooke, label='Matooke', color= "green")
plt.xlabel('Years')
plt.ylabel('Yield (tons per hectare)')
plt.title('Crop Yield in Lwengo')
plt.show()
