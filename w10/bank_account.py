class Person:

  def __init__(self, fn, ln):
    self.first_name = fn
    self.second_name = ln
    self.address = None

  def set_address(self, address):
    self.address = address

  def __str__(self):
    return f"{self.first_name} {self.second_name}"



class IndividualAccount:

  def __init__(self, sort_code, account_number, owner):
    self.sort_code = sort_code
    self.account_number = account_number
    self.owner = owner
    # type - says what class it belongs to
    if type(owner) == "Person":
      self.owner = owner
    else:
      self.owner = None
    self.balance = 0


  def get_account_data(self):
    print(f"The account belongs to {self.owner}. The account number is {self.account_number}. The balance is {self.balance}")

  def pay_in(self, money):
    self.balance += money

  def withdraw(self, money):
    self.withdraw -= money

class SharedAccount:

  def __init__(self, sort_code, account_number):
    self.sort_code = sort_code
    self.account_number = account_number
    self.owner = []
    self.balance = 0

  def pay_in(self, money):
    self.balance += money

  def withdraw(self, money):
    self.withdraw -= money

  def get_account_data(self):
    full_owners =""
    for person in self.owners:
      full_owners + person + ""

    print(f"The shared account belongs to {self.owners}. The account number is {self.account_number}. The balance is {self.balance}")

p1 = Person("Peter", "Predescu")
p2 = Person("John", "Power")
p3 = Person("Maria", "Queen")
p4 = Person("Harry", "Potter")

p1.set_address("There lane,W3 12A ")
print(p1)
print(p2)
print(p3)
print(p4)

acc1 = IndividualAccount("10244042", "10-23-66", p2)
acc2 = IndividualAccount("10244842", "15-46-66", p3)
acc3 = IndividualAccount("10244642", "10-41-66", p4)

acc1.get_account_data()
acc2.get_account_data()
acc3.get_account_data()

acc1.pay_in(10)
acc2.withdraw(50)
acc3.pay_in(18)
