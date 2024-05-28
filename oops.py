# # # class  Animal:

# # #     # class variable 
# # #     name = 'eleaphant'
# # #     weight = 2000 
# # #     age = 25

# # #     # function vs method 
# # #     def display(self):
# # #         print(self.weight)





# # # animal_objects1 = Animal()
# # # animal_objects2 = Animal()


# # # animal_objects1.name = "python"
# # # print(animal_objects1.name)

# # # print(animal_objects2.weight) 






# # # Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# # class  Animal:
# #     # class variable 
# #     num1 = 100
# #     num2 = 200

# #     def __init__(self,name,weigh,age):    # constructor
# #         # instance variable
# #         self.animal_name = name
# #         self.animal_weight = weigh
# #         self.animal_age = age


# #     # function vs method 
# #     def display(self):
# #         print(self.animal_weight)   # obj.animal_weight

# # # obj1 = Animal(name='tiger',weigh=42,age=21)
# # # obj1 = Animal('tiger',90,25)
# # # print(obj1.animal_name)
# # # print(obj1.animal_age)
# # obj2 = Animal('lion',85,42)
# # print(obj2.animal_name)


# # # obj1.animal_weight = 100
# # # obj1.display()

# # print(obj2.num2)
# # # obj1.




# # The self Parameter
# # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# # Example
# # Use the words mysillyobject and abc instead of self:

# # class Person:
# #   def __init__(mysillyobject, name, age):
# #     mysillyobject.name = name
# #     mysillyobject.age = age

# #   def myfunc(abc):
# #     print("Hello my name is " + abc.name)

# # p1 = Person("John", 36)
# # p1.myfunc()




# class Bank:

#     # defining class properties e.g variable
#     name = 'Ranjit Singh'
#     age = 22
#     address = 'Mathura UP'
#     bank_name = 'canara bank'
#     account = 246101041407

#     # Defining method in class
#     def show_info(self):
#         # accessing class properties in method
#         # print(Bank.name)
#         print(self.name)
#         print(self.age)
#         print(self.address)
#         print(self.bank_name)
#         print(self.account)

# #creating object or instance of class
# account_1 = Bank()
# print('name of the account holder :- ',account_1.name,' and account number is :- ',account_1.account)
# print()

# account_1.name = "Ranjit sharma"
# print('account holder name is changed :-',account_1.name,'\n')

# account_1.show_info()
# print()
# print('Second accountant Details  ')

# # creating second object
# account_2 = Bank()
# print(account_2.name)


# #calling the class method
# print('showing account 1 information')
# account_1.show_info()
# print()

# print('showing account 2 information')
# account_2.show_info()
# print()