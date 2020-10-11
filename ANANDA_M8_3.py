import matplotlib.pyplot as plt #mengimport library

#memasukkan data setiap interval sesuai dengan frekuensinya
x = [40, 40, 40, 40, 59, 59,
            59, 59, 59, 59, 69, 69, 
            69, 69, 69, 69, 79, 79, 
            79, 79, 79, 79, 79, 79, 
            89, 89, 89, 89, 100, 100, 
            100, 100, 100]

#membuat grafik histogram menggunakan .hist() dan memasukkan data yang telah dimasukkan tadi bersama jangkauan intervalnya
plt.hist(x, bins = 6)
#memberikan judul pada grafik
plt.title("Data Nilai Mahasiswa")
#memberikan label grafik x dan y
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
#menampilkan grafik
plt.show()