import matplotlib.pyplot as plt 

bahasa = ["Russian", "English", "Korean", "Chinese", "French", "Swahili"]
people = [9, 65, 28, 22, 14, 7]

plt.pie(people, explode=(0, 0, 0, 0, 0, .2), labels = bahasa, autopct="%0.2f%%")
plt.title ("Jumlah sample acak sebanyakn 145 orang\nyang dapat berbahasa asing dengan lancar", bbox = {"facecolor" : "0.9"})

plt.show()