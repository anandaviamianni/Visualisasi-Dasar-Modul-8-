import matplotlib.pyplot as plt 

lake_volume = [84, 127, 50, 124, 112, 263, 74, 194,
                107, 156, 77, 72, 140, 121, 86, 64,
                98, 106, 88, 76, 131, 53, 149, 134,
                125, 53, 95, 256, 113, 89, 126]

plt.boxplot(lake_volume)
plt.title("Volume danau-danau di dunia")

plt.show()