import matplotlib.pyplot as plt #mengimport library

#memasukkan daftar nama negara kedalam list
negara = ["Norway", "Germany", "Canada", "United States", "Netherlands"]
#memasukkan total mendali yang setiap negara dapatkan
totalmendali = [39, 31, 29, 23, 20]

#memasukkan data kedalam .pie() untuk membuat grafik pie chart dan mengkustomisasinya agar pada grafik dapat menampilkan persen
plt.pie(totalmendali, autopct="%0.2f%%")
#membuat judul grafik
plt.title ("Perolehan Mendali Winter Olympics Pyeongchang 2018")
#.legend()digunakan untuk menampilkan data negara sesuai warna yang ditampilkan di pie chart
plt.legend(negara, loc = "lower right", bbox_to_anchor = (1.2, 0))

#menampilkan grafik
plt.show()