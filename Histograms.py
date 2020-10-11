import matplotlib.pyplot as plt 

x = [5, 5, 5, 15, 15, 15, 15, 20, 
            20, 20, 20, 20, 25, 25, 25, 25, 31, 31, 31]

plt.hist(x, bins = 5)
plt.show()