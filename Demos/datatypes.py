print("What is your name?")
#Variable is a container, which can store data for us in the memory (string, intiger,float,bool)
name = input()
print("What is yourage?")
age = int(input())
print("What is your bank balace?")
balance = float(input())

print("Welcome {}. You are set to be {} years old. Your bank balance is {:.2f}.".format(name, age, balance ))