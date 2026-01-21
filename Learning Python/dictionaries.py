pizza = {
    "name": "Hawaiian Pizza",
    "price": 100,
    "calories_per_slice": 200,
    "toppings": ["pineapple", "cheese"]
}
print(pizza)
print(pizza["name"])

pizza["price"] = 300
print(pizza["price"])
print(pizza)


burger = dict([("burger_name", "Angel's Burger"), ("burger_price", 50), ("calories", 100)])
print(burger)


# get, keys, values, items, clear, pop, popitem, update
computer = {
    "cpu": "AMD",
    "ram": 16,
    "peripherals": ["mouse", "keyboard", "headset"]
}

print(computer.get("ram"))
print(computer.keys())
print(computer.values())
print(computer.items())

computer.pop("cpu", "AMD")
print(computer)

computer.popitem()
print(computer)

computer.update({"ram": 32, "color": "RGB"})
print(computer)

computer.clear()
print(computer)