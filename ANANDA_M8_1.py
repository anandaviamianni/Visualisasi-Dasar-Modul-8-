import matplotlib.pyplot as plt #mengimport library matplotlib


#memberikan data untuk x axis
x = [5, 10, 20, 40, 60, 80, 80, 75, 60, 50, 40] 
# memberikan data untuk y axis
y = [5, 15, 25, 45, 60, 85, 85, 70, 65, 60, 30]

plt.plot(x, marker = "o", color = "blue", linewidth = 2.0) #memasukkan data x ke dalam grafik dan mengkustomisasinya
plt.plot(y, marker = "o", color = "green", linewidth = 2.0, linestyle = "--")  #memasukkan data y ke dalam grafik dan mengkustomisasinya
plt.title("Hasil Tes Kecepatan") #memberikan judul grafik

#memberikan label pada sumbu x dan y
plt.xlabel("second")
plt.ylabel("speed")

#menampilkan grafik
plt.show()