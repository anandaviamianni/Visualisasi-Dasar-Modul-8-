import matplotlib.pyplot as plt 

bulan = ["Januari", "Februaari", "Maret", "April"]
harga = [774000, 790000, 842000, 951000]

plt.plot(bulan, harga, marker = "o") #memasukkan data
plt.title("Harga Emas Q1 2020") #memberikan judul

#memberikan label pada sumbu x dan y
plt.xlabel("Bulan")
plt.ylabel("Harga Emas")

plt.show()