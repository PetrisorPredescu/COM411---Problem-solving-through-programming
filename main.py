import matplotlib.pyplot as plt

def read_data(filename):
  f = open(filename, "r")
  content = f.readlines()
  f.close 
  return content

def run():
  data = read_data("w9/temps.txt")
  fig, axes = plt.subplots(1,2)
  x = range(1,8,1)
  y = data
  axes[0].plot(x,data)
  axes[1].bar(x,data)

  plt.show()


run()




