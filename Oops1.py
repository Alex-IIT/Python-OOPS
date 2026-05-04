#Initialize a class
class employee:
    #special function/magic method
    def __init__(self):      #This is called constructor
        self.id=123
        self.salary=50000
        self.department='AI-ML'
        # print(id(self))

    def travel(self,destination):
        print(f"We are travelling to {destination}")

# Creating an Object/instance of class employee
sam=employee()
# print(id(sam))


sam.name="Sam Billings"    # Creating attributes from outside the class
print(sam.name)

#creating another object of class employee and checking its id to see if it is different from the first one
# shaurya=employee()
# print(id(shaurya))


#Printing the atttribute 
# print(sam.department)        

#Calling a method
#sam.travel('kanpur')

