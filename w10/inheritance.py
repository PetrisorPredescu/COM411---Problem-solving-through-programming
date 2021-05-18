class Person:

  def __init__(self, fn, ln):
   self.first_name = fn
   self.second_name = ln
   self.address = None

  def set_address(self, address):
   self.address = address

  def __str__(self):
   return f"{self.first_name} {self.second_name}"

class BankAccount:
  
  def __init__(self, sort_code, account_number):
    self.sort_code = sort_code
    self.account_number = account_number
    self.balance = 0

  def pay_in(self, money):
    self.balance += money

  def withdraw(self, money):
    self.withdraw -= money


class IndividualAccount(BankAccount):

  def __init__(self, sort_code, account_number, owner):

    super().__init__(sort_code, account_number)
    
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



class SharedAccount(BankAccount):

  def __init__(self, sort_code, account_number):
    super().__init__(sort_code, account_number)
    self.owner = []
    
  def get_account_data(self):
    full_owners =""
    for person in self.owners:
      full_owners + person + ""

    print(f"The shared account belongs to {self.owners}. The account number is {self.account_number}. The balance is {self.balance}")

p1 = Person("Peter", "Predescu")

acc1 = IndividualAccount("10244042", "10-23-66", p1)

acc1.get_account_data()
