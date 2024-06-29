class Animal:
    # Constructor
    def __init__(self, name, species):
        self.name = name  # Attribute
        self.species = species  # Attribute
    
    # Method
    def make_sound(self, sound):
        print(f"{self.name} says {sound}")

# Creating an object of the Animal class
dog = Animal("Buddy", "Dog")

# Accessing attributes  
print(f"Name: {dog.name}")
print(f"Species: {dog.species}")

# Calling a method
dog.make_sound("Woof")
