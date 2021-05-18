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


Peter = Person("Peter", 35, 80, 65)
Ramona = Person("Ramona", 36)
Mihai = Person("Mihai")
Tim = Person("Tim", weight = 87)

print(f"The name of Peter is {Peter.age}, whereas the age of Ramona is {Ramona.age}, with Tim being {Tim.age} years old")

