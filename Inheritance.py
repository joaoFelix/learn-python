class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("WUF WUF")


class Cat(Mammal):
    # Python does not like empty classes, so we use this keyword
    pass


dog = Dog()
dog.walk()
dog.bark()