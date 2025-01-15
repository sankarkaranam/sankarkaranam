class Animal:
    def eat(self):
        print("This animal can eat!")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("The dog barks!")

# Example usage
dog = Dog()
dog.eat()  # Inherited from Animal: Output: This animal can eat!
dog.bark()  # Unique to Dog: Output: The dog barks!

#In the above example, we have defined a class Animal with a method eat(). We have defined another class Dog that inherits from the Animal class. The Dog class has a method bark(). We have created an object dog of the Dog class and called the methods eat() and bark() using the object dog. The eat() method is inherited from the Animal class and the bark() method is unique to the Dog class.
#Inheritance is a way to achieve code reusability in Python. It allows a class to inherit the properties and methods of another class. The class that inherits the properties and methods is called the child class or subclass

