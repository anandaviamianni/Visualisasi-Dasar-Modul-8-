import matplotlib.pyplot as plt #mengimport library

# memasukkan data total kerja
lake_volume1 = [10.34,21.01,23.68,24.59,25.29,8.77,26.88,15.04,14.78,10.27,35.26,15.42,18.43,14.83,21.58]

#memasukkan data yang telah dibuat dengan mengkustomisasnya
plt.boxplot([lake_volume1], patch_artist=False,
            showmeans=True, meanline=True, labels=["Male & Female"])
#membuat judul grafik
plt.title("Total Nilai Kerja")
#menampilkan grafik
plt.show()