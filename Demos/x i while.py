# =While loop(and also FOR loop) can be used to have a repetition of a procedure in our code

print("How many times to print the symbol?")
x = int(input())

#i is a counter - it keeps a track how many times we went through the loop
i = 0;

while i < x: #condition for repeting the code as long as i lower than x
  print("\u27bd" , i)
  i = i + 1 #new value of the conuter is one more than it used to be
print("We left the loop")