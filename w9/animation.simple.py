import matplotlib.pyplot as plt
import matplotlib.animations as animation

fig,ax = plt.subplots()

def animate(frame):
  global ax 
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  ax.plot(frame, frame)
  return frame

def run():
  global fig
  simple_animation = animation.Funcanimation(fig, animate, frames = 10, intervals = 1000 )
  plt.show()

run()


