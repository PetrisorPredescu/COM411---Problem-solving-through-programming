#The class i.e. blueprint for my objects
class Person:

  #Class atribute -> constant, visible to all objects of the class
  MAX_ENERGY = 100
  #Initialiser (special instance method, invoked only once, at creation)

  def __init__(self, name, age, weight, energy):
    #Instance attributes
    self.name = name
    self.age = age
    self.weight = weight
    if energy > 100:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy

#Change a constant
Person.MAX_ENERGY = 50
person1 = Person("Peter", 35, 80, 65)
person2 = Person("Ramona", 36, 60, 80)
person3 = Person("Mihai", 28, 90, 22)

print(f"Person 1 has {person1.energy} energy and Person 2 has {person2.energy} energy and Person 3 has {person3.energy}")
