class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f'{self.name} says Woof!'
    
    def get_age(self):
        return f'{self.name} is {self.age} years old.'
    
    def walk(self):
        raise NotImplementedError('Subclass has not been implemented')
    
my_dog = Dog('Buddy', 5)
print(my_dog.bark())
print(my_dog.get_age())
print(my_dog.walk())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f'{self.name} says Woof!'
    
    def get_age(self): #getter method(gets information from self.name and self.age)
        return f'{self.name} is {self.age} years old.'
    
    def walk(self):
        return f'{self.name} is happily going on a walk'
    
    def rename(self, new_name):
        self.name = new_name
        return f'The dog has changed their name to {self.name}'
    
#Inheritance
class ServiceDog(Dog):
    def guide(self):
        return f'Our service dog is trained to guide and assist visually impaired individuals.'
    
    def sit(self):
        return f'{self.name} is trained to sit.'
    
    def bark(self):
        return f'{self.name} barks softly to alert the owner'
    
serviceDog = ServiceDog('James', 3, 'Poodle')
print(serviceDog.bark())
print(serviceDog.sit())