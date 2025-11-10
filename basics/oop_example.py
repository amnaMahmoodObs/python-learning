class MyClass:
    # Class variable
    class_variable = "I am a class variable"

    def __init__(self):
        # Constructor without arguments
        pass

    def display_class_variable(self):
        print(f"Accessing class variable from instance method: {MyClass.class_variable}")
        print(f"Accessing class variable using self: {self.class_variable}")

# Creating an instance of MyClass
obj = MyClass()

# Accessing class variable directly through the class
print(f"Accessing class variable directly: {MyClass.class_variable}")

# Accessing class variable through an instance
print(f"Accessing class variable through instance: {obj.class_variable}")

# Calling a method to display the class variable
obj.display_class_variable()

# Modifying class variable through the class
MyClass.class_variable = "Class variable modified"
print(f"Class variable after modification: {MyClass.class_variable}")
print(f"Instance still sees modified class variable: {obj.class_variable}")
