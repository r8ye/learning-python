class Comics:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == self.pages

comic1 = Comics("The Nice House on the Lake", 100)
comic2 = Comics("The Flash", 250)

print(len(comic1))
print(len(comic2))
print(str(comic1))
print(str(comic2))
print(comic1 != comic2)


class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        return self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in the cart")

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

# adding
cart = Cart()
cart.add("Apple")
cart.add("Mango")
cart.add("Banana")
cart.add("Strawberry")
cart.add("Melon")
print(cart.list_items())

# removing
cart.remove("Apple")
print(cart.list_items())

cart.remove("banana")

# length
print(len(cart))

# get item
print(cart[2])

# contains
print("melon" in cart)
print("Melon" in cart)

# iterate
for item in cart:
    print(item)

for item in cart:
    print(item, end = " ")