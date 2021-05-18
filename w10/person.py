#The class i.e. blueprint for my objects
class Person:

  #Class atribute -> constant, visible to all objects of the class
  MAX_ENERGY = 100
  #Initialiser (special instance method, invoked only once, at creation)

  def __init__(self, name, age = 0, weight = 10, energy = 50):
    #Instance attributes
    self.name = name
    self.age = age
    self.weight = weight
    if energy > 100:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy
  
  def hello(self):
    print(f"Hello, my name is {self.name}. I am {self.age} years old and I weight {self.weight} kg. Nice to meet you!")

  def grow(self):
    self.age += 1

  def eat(self, food, weight):
    self.weight += weight
#The class i.e. blueprint for my objects
class Person:

  