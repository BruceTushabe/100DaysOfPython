from matplotlib import pyplot as plt

import pandas as pd

import seaborn as sns

df = pd.read_csv('kiva_data.csv')

df.head()

f, ax = plt.subplots(figsize = (115, 10))
sns.barplot(data=df, x='country', y='loan_amount')

import matplotlib.ticker as mtick

f, ax = plt.subplots(figsize=(15, 10))

# Plot the data

sns.barplot(data=df, x="Country", y= "loan amount")

# Use part of the code above to format the y-axis ticks below this line

import matplotlib.ticker as mtick
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
# Set color palette
sns.set_palette("Pastel1")

# Set style
sns.set_style("whitegrid")

# Create figure and axes (no need to use the previous syntax, as the y-label ticks aren't going to be formatted)
plt.figure(figsize=(25, 15))
plt.xlabel("Country")
plt.ylabel("Loan Amount")

# Add a title
plt.title("Kiva Loans by Country")

# Use Seaborn to create the bar plot
sns.barplot(data=df, x="country", y="loan_amount", hue="gender")

plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="country", y="loan_amount", hue="gender")
sns.set_palette("Pastel2")

# Box Plot by Activity
plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="activity", y="loan_amount", hue="gender")

# Violin Plots
plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="activity", y="loan_amount")

plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="country", y="loan_amount")

# Split Violin Plots
# Some styling (feel free to modify)
sns.set_palette("Spectral")
plt.figure(figsize=(18, 12))

sns.violinplot(data=df, x="country", y="loan_amount", hue="gender", split=True)



