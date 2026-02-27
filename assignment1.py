import numpy as np
import matplotlib.pyplot as plt


# my data

x = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
     2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
     2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
     2020, 2021, 2022, 2023, 2024]

c = [4172, 4270, 4375, 3553, 3402, 2840, 1959, 1963, 1607, 1353,
     1228, 1195, 1186, 1248, 1235, 1180, 1164, 1268, 1296, 1152,
     1311, 1194, 1212, 1555, 1627, 1380, 1304, 1125, 1072, 931,
     799, 755, 714, 672, 457]

n = [12889, 12311, 11380, 11521, 12885, 12680, 14081, 14754,
     15140, 15203, 15773, 15464, 14202, 14292, 13238, 13022,
     12428, 11466, 11030, 9146, 9395, 9007, 8821, 9030, 8653,
     8418, 8269, 8496, 8972, 8718, 8240, 8201, 7268, 7128, 7308]

e = [8655, 8563, 8194, 8328, 8082, 8654, 9004, 9189, 9216,
     9542, 9812, 9573, 9473, 9396, 9584, 9976, 9879, 9699,
     9815, 8576, 8989, 8806, 8466, 8339, 7997, 7991, 8024,
     7929, 7902, 7941, 7372, 7579, 7369, 7271, 7072]

p = [8242, 8729, 8334, 8592, 8253, 7066, 7058, 6315, 6379,
     5374, 6039, 6611, 6248, 6899, 6918, 6282, 6099, 6095,
     5895, 2388, 2398, 2276, 2210, 2236, 2198, 2217, 2146,
     2116, 2123, 2099, 2102, 2140, 1961, 2081, 2128]

# multiple line graph

plt.plot(x, c, label='Coal')
plt.plot(x, n, label='Natural gas')
plt.plot(x, e, label='Electricity')
plt.plot(x, p, label='Petroleum products')

plt.xlabel('Year')
plt.ylabel('Energy sector')
plt.title('Energy consumption by sector and fuel 1990-2024')

plt.legend()
plt.grid(True)

plt.show()

# 1990 vs 2024 pie charts

values1 = np.array([4172, 12889, 8655, 8242])
labels = ['Coal', 'Natural gas', 'Electricity', 'Petroleum products']

values2 = np.array([457, 7308, 7072, 2128])

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].pie(values1, labels=labels, autopct='%1.1f%%', startangle=90)
axes[0].set_title('1990 Energy consumption by sector and fuel')

axes[1].pie(values2, labels=labels, autopct='%1.1f%%', startangle=90)
axes[1].set_title('2024 Energy consumption by sector and fuel')

plt.tight_layout()
plt.show()

# 1990 vs 2024 bar chart

values1 = np.array([4172, 12889, 8655, 8242])
values2 = np.array([457, 7308, 7072, 2128])
labels = ['Coal', 'Natural gas', 'Electricity', 'Petroleum products']

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - width/2, values1, width, label='1990')

ax.bar(x + width/2, values2, width, label='2024')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Energy consumed')
ax.set_title('1990 vs 2024 Energy consumption by sector and fuel')
ax.legend()

plt.tight_layout()
plt.show()