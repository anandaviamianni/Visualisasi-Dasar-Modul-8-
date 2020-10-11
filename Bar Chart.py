import numpy as np 
import matplotlib.pyplot as plt

objek = ("python", "jawva", "c++", "perl", "scala", "lisp")
y_pos = np.arange(len(objek))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align = "center", alpha = 0.5)
plt.xticks(y_pos, objek)
plt.ylabel("Usage")
plt.title("Programming language usage")

plt.show()