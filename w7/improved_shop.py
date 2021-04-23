import json

def shop():
  with open("items.json") as json_file:
   items = json.load(json_file) 
  return items 

  return items

def save_items(items = {}):
  json_database = open("items.json", "w")
  json.dump(items, json_databse, indent = 4)
  json.database.close()

def view_all(products={}):
  for i in products:
    print(i)

view_all(shop())

def basket():
  basket = []
  while True:
    item = input("Enter item (or \"stop\"): ")
    if item == "stop":
      break
    else: 
      basket.append(item)
  return basket

def till(basket = []):
  shoplist = shop()
  total = 0.0
  for item in basket:
    print(shoplist[item])
    total += shoplist[item]
  return total

def run():
  print("Welcome to Pete's shop! Please have a look around and add item you like!")
  chosen_items=basket()
  while True:
    print("Are you ready to pay?")
    if input().lower() == "yes":
      to_pay = till(chosen_items)
      print(f"Please pay ${to_pay:.2f} by cash or card")
      break
    else:
      chosen_items += basket()

run()
