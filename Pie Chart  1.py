import matplotlib.pyplot as plt 

bahasa = ["Russian", "English", "Korean", "Chinese", "French", "Swahili"]
people = [9, 65, 28, 22, 14, 7]

plt.pie(people, autopct="%0.2f%%")
plt.title ("Jumlah sample acak sebanyakn 145 orang\nyang dapat berbahasa asing dengan lancar")
plt.legend(bahasa, loc = "lower right", bbox_to_anchor = (1.2, 0))

plt.show()