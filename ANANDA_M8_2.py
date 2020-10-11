import matplotlib.pyplot as plt  #mengimport library
import numpy as np 

TotalPenjualan = [10, 13, 15, 17, 18, 11, 13, 15, 17, 18, 12, 14, 15, 17, 18, 12, 14, 16, 17, 12] #memasukkan data penjualan kedalam list
temperature = [27, 28.9, 34.5, 44.1, 42.4, 25.3, 32.9, 37.5, 38.1, 43.4, 32.6, 38.2, 37.5, 44.1, 43.4, 30.6, 32.2, 42.8, 43.1, 31.6] #memasukkan data temperature suhu kedalam list

plt.scatter(TotalPenjualan, temperature) #menempatkan data yang telah dibuat kedalam figure
plt.title("Temperature vs Penjualan") #membuat judul grafik
#membuat label grafik x dan y
plt.xlabel("Penjualan") 
plt.ylabel("Temperature")
#membuat data korelasi 
data = np.array([TotalPenjualan,temperature])
#menampilkan grafik
plt.show()
#menampilkan data korelasi
print("Kolerasi : \n\n", np.corrcoef(data))
