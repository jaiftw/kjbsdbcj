# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values:

# thisdict = {
#   "name": "Mohan",
#   "Branch": ("CSE","IT"),
#   "year": 2
# }
# print(thisdict) 
# print(type(thisdict))

# Dictionary Items

# print(thisdict["Branch"])
# thisdict = {
#   "name": "Mohan",
#   "Branch": "CSE",
# #   "year": 2,               -->overwrite kardeta hai
#   "year": 3
# }
# # print(thisdict) 

# # Dictionary Length
# # To determine how many items a dictionary has, use the len() function:

# # Example
# # Print the number of items in the dictionary:

# print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# Example
# String, int, boolean, and list data types:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"],
#   "type" : ("1","2","3"),
#   "set" : {"1",True,"hello"}
# }

# print(thisdict)



# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

# Example
# Using the dict() method to make a dictionary:

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)





# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# ExampleGet your own Python Server
# Get the value of the "model" key:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)
# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:

# x = thisdict.get("model")
# print(x)




# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example
# Get a list of the keys:

# x = thisdict.keys()
# print(x)





# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change



# Get Values
# The values() method will return a list of all the values in the dictionary.

# Example
# Get a list of the values:

# x = thisdict.values()




# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change




# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

# Example
# Get a list of the key:value pairs

# x = thisdict.items()


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.items()

# print(x)






# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example
# Update the "year" of the car by using the update() method:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})






# Removing Items
# There are several methods to remove items from a dictionary:

# ExampleGet your own Python Server
# The pop() method removes the item with the specified key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)






# The del keyword removes the item with the specified key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)




# Example
# The del keyword can also delete the dictionary completely:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.





# The clear() method empties the dictionary:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)