# Parent Class: Entity
class Entity:
    def move(self):
        pass

# Vehicle Classes
class Bus(Entity):
    def move(self):
        print("Driving")


class Lorry(Entity):
    def move(self):
        print("Flying")

class Plane(Entity):
    def move(self):
        print("Flying")

class Boat(Entity):
    def move(self):
        print("Sailing")

class Bike(Entity):
    def move(self):
        print("Riding")


# Animal Classes
class Cat(Entity):
    def move(self):
        print("Running")


class Bat(Entity):
    def move(self):
        print("Flying")

class Snake(Entity):
    def move(self):
        print("Slithering")

class Fish(Entity):
    def move(self):
        print("Swimming")

# Testing Polymorphism
entities = [Bus(), Lorry(), Plane(), Boat(), Bike(), Cat(), Bat(), Snake(), Fish()]

for e in entities:
    e.move()
