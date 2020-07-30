class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print(f"({self.x},{self.y})")


point1 = Point(10, 20)
point1.draw()

class Person:

    def __init__(self, name):
        self.name = name

    def talk(self, message):
        print(f'{self.name}: {message}')

jf = Person("Obi-wan Kenobi")
jf.talk("Hello there!")
