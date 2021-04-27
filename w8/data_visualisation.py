import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,10.65]
y = [10,15,18,20,25,36,80,90.88]

plt.xlabel("Age")
plt.ylabel("Score")

plt.plot(x,y,"gD")

plt.show()