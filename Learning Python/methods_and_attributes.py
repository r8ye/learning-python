# class and instance attribute
class Planet:
    color = "Red"

    def __init__(self, name):
        self.name = name

print(Planet.color)

planet1 = Planet("Earth")
print(planet1.name)
print(planet1.color)

planet2 = Planet("Mars")
print(planet2.name)
print(planet2.color)


class Motorcycle:
    def __init__(self, motor, types):
        self.motor = motor
        self.types = types

motorcyle1 = Motorcycle("QJMOTOR SRV200", "cruiser")
motorcyle2 = Motorcycle("Honda Click 125i", "scooter")

print(motorcyle1.motor)
print(motorcyle1.types)

print(motorcyle2.motor)
print(motorcyle2.types)


# method
class Car:
    def __init__(self, model, seats):
        self.model = model
        self.seats = seats

    def describe(self):
        return f"I love riding the {self.model}. It has {self.seats} seats."

car1 = Car("Miata", 2)
car2 = Car("BMW M3", 4)

print(car1.describe())
print(car2.describe())