from person import Person

class Database:

  def __init__(self):
    self.name = "Peter's Database"
    self.people = []
    self.suspended = []

  def add_person(self, person):
    self.people.append(person)

  def display_all(self):
    for person in self.people:
      person.hello()

  def all_eat(self, food, weight):
    for person in self.people:
      person.eat(food, weight)


db = Database()
Daniel = Person("Daniel", 26, 77)
Raluca = Person("Raluca", 23, 48, 99)
Piotr = Person("Piotr")
Vlad = Person("Vlad", 42, 150)

db.add_person(Daniel)
db.add_person(Raluca)
db.add_person(Piotr)
db.add_person(Vlad)
db.display_all()
print()
db.all_eat("Lasagna", 3)
print()
db.display_all()

