# dictionaries looping
products = {
    "Laptop": 30000,
    "Iphone": 25000,
    "Ipad": 15000,
    "Tablet": 10000
}

for price in products.values():
    print(price)

for product in products.keys():
    print(product)

for item in products.items():
    print(item)

for product, price in products.items():
    print(product, price)

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)


for product in enumerate(products):
    print(product)

for product, price in enumerate(products.items()):
    print(product, price)

for price in enumerate(products.values()):
    print(price)

# kapag may index separate yong number hindi nakalagay sa tuple yong index
for index, product in enumerate(products.items()):
    print(index, product)

for index, price in enumerate(products.values()):
    print(index, price)

# start sa 2
for index, product in enumerate(products.items(), 2):
    print(index, product)



# sets
sets = {1, 2, 3, 4, 5}

sets.add(8)
print(sets)

sets.remove(4)
print(sets)

# sets.clear()
# print(sets)


# issubset, issuperset, isdisjoint
set_a = {5, 4, 3, 2, 1}
set_b = {9, 1, 0, 2, 4}
set_c = {1, 2, 3}
set_d = {7, 6, 8}

print(set_c.issubset(set_a))
print(set_a.issubset(set_c))
print(set_a.issuperset(set_c))
print(set_c.issuperset(set_b))
print(set_a.isdisjoint(set_d))
print(set_b.isdisjoint(set_c))


# union - combine
print(set_c | set_d)

# intersection - common
print(set_a & set_b)

# difference - not in the other set
print(set_c - set_d)
print(set_a - set_b)

# symmetric - not in both sets
print(set_a ^ set_b)

# |= &= -= ^=
set_a &= set_b
print(set_a)

# present or not
print(5 in set_c)
print(0 in set_b)



grades = dict([("stats", 1.25), ("ethics", 2.5), ("math", 1.5)])

print(grades)
print(grades.keys())


# looping
items = {
    "biscuit": 10,
    "coke": 25,
    "candy": 1
}

for presyo in items.values():
    print(presyo)

for index, presyo in enumerate(items.items()):
    print(index, presyo)

for index, presyo in enumerate(items.items(), 1):
    print(index, presyo)

print(items.clear())