import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# my data


df = pd.read_csv("ecukdata.csv")


# multiple line graph


plt.plot(df['Year'], df['Coal'], label='Coal')
plt.plot(df['Year'], df['Natural gas'], label='Natural gas')
plt.plot(df['Year'], df['Electricity'], label='Electricity')
plt.plot(df['Year'], df['Petroleum products'], label='Petroleum products')

plt.xlabel('Year')
plt.ylabel('Energy consumption (kteo)')
plt.title('Energy consumption by sector and fuel 1990–2024')

plt.legend()
plt.grid(True)

plt.show()


# selecting 1990 and 2024 data


row_1990 = df[df['Year'] == 1990].iloc[0]
row_2024 = df[df['Year'] == 2024].iloc[0]

labels = ['Coal', 'Natural gas', 'Electricity', 'Petroleum products']

values_1990 = [
    row_1990['Coal'],
    row_1990['Natural gas'],
    row_1990['Electricity'],
    row_1990['Petroleum products']
]

values_2024 = [
    row_2024['Coal'],
    row_2024['Natural gas'],
    row_2024['Electricity'],
    row_2024['Petroleum products']
]


# 1990 vs 2024 pie charts


fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].pie(values_1990, labels=labels, autopct='%1.1f%%', startangle=90)
axes[0].set_title('1990 Energy consumption by sector and fuel')

axes[1].pie(values_2024, labels=labels, autopct='%1.1f%%', startangle=90)
axes[1].set_title('2024 Energy consumption by sector and fuel')

plt.tight_layout()
plt.show()


# 1990 vs 2024 bar chart


x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, values_1990, width, label='1990')
plt.bar(x + width/2, values_2024, width, label='2024')

plt.xticks(x, labels)
plt.ylabel('Energy consumed (kteo)')
plt.title('1990 vs 2024 Energy consumption by sector and fuel')
plt.legend()

plt.tight_layout()
plt.show()