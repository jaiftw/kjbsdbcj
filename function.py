# # # # # # # Python Functions
# # # # # # # A function is a block of code which only runs when it is called.

# # # # # # # You can pass data, known as parameters, into a function.

# # # # # # # A function can return data as a result.

# # # # # # # Creating a Function
# # # # # # # In Python a function is defined using the def keyword:

# # # # # # # ExampleGet your own Python Server
# # # # # # def my_function():
# # # # # #   print("Hello from a function")

# # # # # # ##calling a function
# # # # # # my_function()





# # # # # Arguments
# # # # # Information can be passed into functions as arguments.

# # # # # Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# # # # # The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# # # # # Example
# # # # # def my_function(fname):
# # # # #   print(fname + " Refsnes")

# # # # # my_function("Emil")
# # # # # my_function("Tobias")
# # # # # my_function("Linus")



# without parameter
# def add():
#     num1 = 10
#     num2 = 20
#     result = num1 + num2
#     return result

# output = add()
# print(output)



# def add(num1 ,num2 ):

#     result = num1 + num2
#     return result


# nu1 = 1
# nu2 = 2
# output = add( 1,2)
# print(output)



# # # # Parameters or Arguments?
# # # # The terms parameter and argument can be used for the same thing: information that are passed into a function.

# # # # From a function's perspective:

# # # # A parameter is the variable listed inside the parentheses in the function definition.

# # # # An argument is the value that is sent to the function when it is called.





# # # Number of Arguments
# # # By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# # # Example
# # # This function expects 2 arguments, and gets 2 arguments:

# # # def my_function(fname, lname):
# # #   print(fname + " " + lname)

# # # my_function("Emil", "Refsnes")



# # # If you try to call the function with 1 or 3 arguments, you will get an error:
# # # Example
# # # This function expects 2 arguments, but gets only 1:

# # # def my_function(fname, lname):
# # #   print(fname + " " + lname)

# # # my_function("Emil")



# # # Arbitrary Arguments, *args
# # # If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# # # This way the function will receive a tuple of arguments, and can access the items accordingly:

# # # Example
# # # If the number of arguments is unknown, add a * before the parameter name:

# # # def my_function(*kids):
# # #   print("The youngest child is " + kids[2])

# # # my_function("Emil", "Tobias", "Linus")
# # # Arbitrary




# # Keyword Arguments
# # You can also send arguments with the key = value syntax.

# # This way the order of the arguments does not matter.

# # Example
# # def my_function(child3, child2, child1):
# #   print("The youngest child is " + child3)

# # my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")



# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:

# Example
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")




# def apna_min(lst):
#     #block of code 
# Initialize minimum with the first element of the list
#     minimum = x[0] 
#     for  i in lst:
#         if minimum > i:
#             minimum = i

#     return minimum
# x = [10,76,25,66,89,90,12,14,18,26,4,8,21,9]
# apna_min(x)






# def square_element(input_list):
#     temp = []
#     for x in input_list:
#         temp.append(x**2)
#     return temp
    

# output = square_element([5,2,3,4])
# print(output)




# def avg_fun(input_lst):
#     return sum(input_lst)/len(input_lst)

# avg_fun([25, 4, 9, 16])




# x = [25, 4, 9, 16]
# temp = 0
# for i in x:
#     temp+=i
# temp/len(x)