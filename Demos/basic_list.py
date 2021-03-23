#Define an empty list
fruits = []

#Define a list with items
vegetables = ["Carrot", "Peas"]

#Add items to the list

fruits.append("Apple")
fruits.append("Bananas")
fruits.append("Tomatoe")
fruits.append("Banana")
print(fruits)

#Remove an item from the list
fruits.remove("Bananas")

print(fruits)

#Remove item by index
del fruits[1]
print(fruits)

#Insert a value not at the print
fruits.insert(1, "Pineapple")

#Acces single element
print(fruits[0])