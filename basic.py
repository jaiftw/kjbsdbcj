# print("hello world")
# var1 = 10
# var2 = 22.3
# var3 = True
# var4 = "Upflairs"
# var5 = 'Company'
# var6 = """Upflairs"""

# print(var1)
# print(var2)
# print(var3)
# print(var4)
# print(var5)
# print(var6)

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(type(var5))
# print(type(var6))

# rupees = 2000
# print("i have",rupees, "rupees")

# paragraph = """welcome to the college,
# goodmorning to all
# todays topic is this """
# print(paragraph)


# college = "Manipal University"
# print(college.upper())
# print(college.lower())
# print(len(college))
# print(college.count("i"))
# print(college.endswith('l'))    -> ye puchna hai 

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# college_name = "  jecrc foundation  "
# # print(college_name.strip())
# # print(college_name.rstrip())
# print(college_name.lstrip())


#indexing 
# college = "manipal uni"
# # m a n i p a l u n i 
# # 0  1  2  3  4  5  6  7  8  9 
# # -9  -8  -7 -6 -5 -4 -3 -2 -1
# print(college[0:4])
# # print(college[4:7])

# print(college[:-6])

# name = "laxmidevi"
# print(name[-3:-1])

# quotes ke ander quotes --> surrondings quotes se match nahi hone chaiye 
# print("'hello may name is jai'")


# String Concatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " & " + b
# print(c)


# F-Strings

# age = 36
# txt = "My name is John, I am " + age     --> ye error dega kyuki apan str to str concat kar sakte hai only 
# print(txt)


# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)


# Escape Character 
# txt = "We are the so-called "Vikings" from the north."        --> ye error dega kyuki apan ne phele quotes me padha tha ki apan quotes ke quotes jab he daal skate hai jab usske surrondings same quotes na ho 


#so issko deal karne ke liye apan escape characters laaye 

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)



# Python Booleans
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# print(bool("Hello"))
# print(bool(15))

# x = "12"
# y = 15.3

# print(bool(x))
# print(bool(y))



# Python Operators
# print(10 + 5)

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	


# Python Assignment Operators

# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3
# :=	print(x := 3)	x = 3
# print(x)

# y = 3
# y+=4
# print(y)

# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example	
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y



# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# x = 5

# print(x > 3 and x < 10)


# x = 5

# print(not(x > 3 and x < 10))

#