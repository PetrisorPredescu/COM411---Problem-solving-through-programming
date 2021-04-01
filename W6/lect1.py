phonebook = {}

while True:
  name = input("Enter a name ")
  number = input("Enter the number: ")
  phonebook[name] = number
  if input("Type 'x' to stop") == 'x':
    break

print (phonebook)

def calling(n, book = {}):
  print(f"Calling {n} with the phone number {book[n]}")

calling ("Peter", phonebook)
