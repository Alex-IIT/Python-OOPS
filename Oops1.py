#Initialize a class
class employee:
    #special function/magic method
    def __init__(self):      #This is called constructor
        self.id=123
        self.salary=50000
        self.department='AI-ML'

    def travel(self,destination):
        print(f"We are travelling to {destination}")

# Creating an Object/instance of class employee
sam=employee()

#Printing the atttribute 
# print(sam.department)        

#Calling a method
#sam.travel('kanpur')

print(type(sam))