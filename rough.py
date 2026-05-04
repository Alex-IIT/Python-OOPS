lst=[12,15,2,6,5]
my_str="Mlops"
my_int=206

# print(type(my_int))
# lst.capitalize()
# my_str=my_str.capitalize()
# print(my_str)

# a="x"
# b="y"
# print(a+b)

#importing a class from another file
# from Oops_project import chatbook
# user1=chatbook()

#accessing private variable from outside the class
# print(user1._chatbook__name)

#using getter and setter to access private variable
# print(user1.getname())
# print(user1.setname("Shaurya Srivastava"))
# print(user1.getname())

from Oops_project import chatbook
user1=chatbook()
print(user1.id)

#Using static method directly from the class without creating an object
chatbook.set_id(100)
user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)