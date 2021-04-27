import matplotlib.pyplot as plt

x = ("Lithuania","Romania","Poland","Bangladesh","Brazil","Colombia","Others")

data = [2,17,1,2,2,2,6]

plt.pie(data, labels = x, explode = [0.1,0.3,0.5,0.7,0.9,1.1,1.2])

plt.show()