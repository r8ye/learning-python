class Wallet:
   def __init__(self, balance):
       self._balance = balance # For internal use by convention

   def deposit(self, amount):
       if amount > 0:
           self._balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self._balance -= amount # Remove from the balance safely

account = Wallet(100)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)

print(my_circle.radius)
print(my_circle.area)
