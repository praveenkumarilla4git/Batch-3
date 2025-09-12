# A list is a collection of items (elements) stored in a single variable
# A list is an ordered and changeble collection. its the most flexible and commonly used type.
#mutable
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)
fruits[1] = "mango"
fruits.append("orange")
print(fruits)
# list --> with different data types
my_list = [10, 3.14, "hello", True]
print(my_list)
print(my_list[0])

# Tuples --> A tuple is an ordered but unchangeable collection.
mapcoordinates = (10.0, 20.5)
print(mapcoordinates)


###########Dictionaries#############
#Dictionaries --> Key value pairs
student = {"name": "Sai", "Age": 15, "grade": "A" }
print(student)

#####Sets#####
# A set unordered and unindexed collection only unique
colors = {"red", "green", "blue", "red"}

colors.add("yellow")
print(colors)