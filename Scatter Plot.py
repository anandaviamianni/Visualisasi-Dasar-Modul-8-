import matplotlib.pyplot as plt 
TotalPenjualan = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]
SuhuPerHari = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]

plt.scatter(TotalPenjualan, SuhuPerHari)
plt.title("Suhu vs Total Penjualan")
plt.xlabel("Suhu per Hari")
plt.ylabel("Total Penjualan")

plt.show()