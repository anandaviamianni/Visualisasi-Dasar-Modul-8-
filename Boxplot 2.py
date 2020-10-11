import matplotlib.pyplot as plt 

lake_volume1 = [84, 127, 50, 124, 112, 263, 74, 194,
                107, 156, 77, 72, 140, 121, 86, 64,
                98, 106, 88, 76, 131, 53, 149, 134,
                125, 53, 95, 256, 113, 89, 126]

lake_volume2 = [104, 147, 70, 144, 132, 24, 94, 214,
                127, 176, 97, 92, 160, 141, 106, 84,
                118, 126, 108, 96, 151, 73, 169, 154,
                145, 73, 115, 18, 133, 109, 146]

plt.boxplot([lake_volume1, lake_volume2], patch_artist=False,
            showmeans=True, meanline=True, labels=["USA", "Canada"])
plt.title("Volume danau-danau di dunia")
plt.show()