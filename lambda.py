# # # # Python Lambda
# # # # A lambda function is a small anonymous function.

# # # # A lambda function can take any number of arguments, but can only have one expression.



# # # # lambda arguments : expression


# # # ExampleGet your own Python Server
# # # Add 10 to argument a, and return the result:

# # # x = lambda a : a + 10
# # # print(x(5))


# # Lambda functions can take any number of arguments:

# # Example
# # Multiply argument a with argument b and return the result:

# # x = lambda a, b : a * b
# # print(x(5, 6))



# # Example
# # Summarize argument a, b, and c and return the result:

# # x = lambda a, b, c : a + b + c
# # print(x(5, 6, 2))




# Example
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))