class Robot:

  # A Class attributes
  laws = "New Robot City. Protect, Obey and Service"

  # A Static Method
  def the_laws():
    print(Robot.laws)

  # a class method
  def assemble(cls):
    return cls("Assemble Robot")

  # An initialiser (special instance method)
  def __init__(self, name=Robot):
    # an instance Attributes
    self.name = name
    self.age = 0

  # an instance method
  def display(self):
    print(f"I am {self.name}")

 
