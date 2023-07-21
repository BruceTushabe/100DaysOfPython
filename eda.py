import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)


df = pd.read_csv("car_data.csv")

# To display the top 5 rows

df.head(5)


