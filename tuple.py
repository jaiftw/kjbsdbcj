# # # # # Tuple
# # # # # Tuples are used to store multiple items in a single variable.

# # # # # Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# # # # # A tuple is a collection which is ordered and unchangeable.

# # # # # Tuples are written with round brackets.

# # # # # ExampleGet your own Python Server
# # # # # Create a Tuple:

# # # # # thistuple = ("apple", "banana", "cherry")
# # # # # print(thistuple)


# # # # # Tuple Items
# # # # # Tuple items are ordered, unchangeable, and allow duplicate values.

# # # # # Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# # # # # Ordered
# # # # # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# # # # # Unchangeable
# # # # # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# # # # # Allow Duplicates
# # # # # Since tuples are indexed, they can have items with the same value:

# # # # # Example
# # # # # Tuples allow duplicate values:

# # # # # thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# # # # # print(thistuple)


# # # # Tuple Length
# # # # To determine how many items a tuple has, use the len() function:

# # # # Example
# # # # Print the number of items in the tuple:

# # # # thistuple = ("apple", "banana", "cherry")
# # # # print(len(thistuple))
# # # # Create Tuple With One Item
# # # # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# # # # Example
# # # # One item tuple, remember the comma:

# # # # thistuple = ("apple",)
# # # # print(type(thistuple))

# # # # #NOT a tuple
# # # # thistuple = ("apple")
# # # # print(type(thistuple))
# # # # Tuple Items - Data Types
# # # # Tuple items can be of any data type:

# # # # Example
# # # # String, int and boolean data types:

# # # # tuple1 = ("apple", "banana", "cherry")
# # # # tuple2 = (1, 5, 7, 9, 3)
# # # # tuple3 = (True, False, False)
# # # # A tuple can contain different data types:

# # # # Example
# # # # A tuple with strings, integers and boolean values:

# # # # tuple1 = ("abc", 34, True, 40, "male")
# # # # type()
# # # # From Python's perspective, tuples are defined as objects with the data type 'tuple':

# # # # <class 'tuple'>
# # # # Example
# # # # What is the data type of a tuple?

# # # # mytuple = ("apple", "banana", "cherry")
# # # # print(type(mytuple))
# # # # The tuple() Constructor
# # # # It is also possible to use the tuple() constructor to make a tuple.

# # # # Example
# # # # Using the tuple() method to make a tuple:

# # # # thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# # # # print(thistuple)


# # # # Access Tuple Items



# # # # Change Tuple Values
# # # # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.


# # # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# # # ExampleGet your own Python Server
# # # Convert the tuple into a list to be able to change it:

# # # x = ("apple", "banana", "cherry")
# # # y = list(x)
# # # y[1] = "kiwi"
# # # x = tuple(y)

# # # print(x)
# # # Add Items
# # # Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# # # 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

# # # Example
# # # Convert the tuple into a list, add "orange", and convert it back into a tuple:

# # # thistuple = ("apple", "banana", "cherry")
# # # y = list(thistuple)
# # # y.append("orange")
# # # thistuple = tuple(y)
# # # 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# # # Example
# # # Create a new tuple with the value "orange", and add that tuple:

# # # thistuple = ("apple", "banana", "cherry")
# # # y = ("orange",)
# # # thistuple += y

# # # print(thistuple)
# # # Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.




# # Remove Items
# # Note: You cannot remove items in a tuple.

# # Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# # Example
# # Convert the tuple into a list, remove "apple", and convert it back into a tuple:

# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.remove("apple")
# # thistuple = tuple(y)
# # Or you can delete the tuple completely:

# # Example
# # The del keyword can delete the tuple completely:

# # thistuple = ("apple", "banana", "cherry")
# # del thistuple
# # print(thistuple) #this will raise an error because the tuple no longer exists



# Python - Join Tuples
# Join Two Tuples
# To join two or more tuples you can use the + operator:

# ExampleGet your own Python Server
# Join two tuples:

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)
# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Example
# Multiply the fruits tuple by 2:

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# lst1 = [1,2,3,4,5]
# print(lst1*2)

# tpl2 = (10,20,30,40)
# print(tpl2*4)