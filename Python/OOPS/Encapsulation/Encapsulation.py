#Encapsulation means hiding the data and allowing access through methods only.
#Encapsulation is a way to achieve data hiding in Python.
#Encapsulation is defined as restricting access to methods and variables in a class. This prevents the data from being modified directly and can only be modified by the methods present in the class.
#Encapsulation can be achieved by using private variables and private methods in a class.
#Private variables are those variables that are accessible only within the class and not outside the class.
#Private methods are those methods that are accessible only within the class and not outside the class.
#To define a private variable, use double underscore __ before the variable name.
#To define a private method, use double underscore __ before the method name.
#To access private variables and methods, use the object of the class.
#Encapsulation is used to protect the data from being modified directly.

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
s = Student
s = Student("Sankar", 25)
s.display()
s.setAge(30)

print("Updated Age:", s.getAge())
s.setName("Sankar")
print("Updated Name:", s.getName())
#Output: 
# Name: Sankar
# Age: 25
# Updated Age: 30
# Updated Name: Sankar
#In the above example, we have defined a class Student with two private variables __name and __age. We have defined two methods setAge() and getAge() to set and get the age of the student. 
# We have defined two methods setName() and getName() to set and get the name of the student. We have created an object s of the class Student and called the methods to set and get the name and age of the student. 
# We have displayed the name and age of the student using the display() method.




#Encapsulation is a way to achieve data hiding in Python.
#Encapsulation is defined as restricting access to methods and variables in a class. This prevents the data from being modified directly and can only be modified by the methods present in the class.
#Encapsulation can be achieved by using private variables and private methods in a class.
#Private variables are those variables that are accessible only within the class and not outside the class.

