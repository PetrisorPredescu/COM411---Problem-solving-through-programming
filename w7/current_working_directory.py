import os
path = os.getcwd()
print(f"Current working directory: {path}")

for file in os.listdir(path):
  print(file)
