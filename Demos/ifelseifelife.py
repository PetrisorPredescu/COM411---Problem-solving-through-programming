print("What is your name")
n = input()
#bool is a boolean datatype - only for True/False

if len(n) > 9: #allow lenght of exactly 9 and grater
  print("You have a very looooong name")
  print("Your name contains {} letters".format(len(n)))
elif len(n) > 2:
  print("Your name is a bit long. Consider a nickname")
elif len(n) > 6:
  print("Your name is very short")
else:
  print("Your name is quite okay")
print("This is the END of the program")
