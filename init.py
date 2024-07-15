class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Tạo một đối tượng Person
person1 = Person("Alice", 30)
person1.introduce()  # Output: My name is Alice and I am 30 years old.

# Tạo một đối tượng Person khác
person2 = Person("Bob", 25)
person2.introduce()  # Output: My name is Bob and I am 25 years old.
