dev = ("Alex", 21, "Software Dev")
print(dev[1])

nums = (1, 2, 3, 4, 5)
print(nums[-3])

name = "Rachelle"
print(tuple(name))

prog_lang = ("C++", "Python", "Java")
print("python" in prog_lang)
print("Python" in prog_lang)

bio = ("Rachelle Fraga", 21, "Computer Science", "TFVC", 3.00)
fullname, age, program, *rest = bio

print(fullname)
print(age)
print(program)

print(rest)


foods = ("ice cream", "chocolate", "candies", "pizza", "pasta")
print(foods[1:4])


# count
rgb = ("red", "blue", "green", "blue")
print(rgb.count("blue"))
print(rgb.count("pink"))


# index
drinks = ("coffee", "milktea", "milk", "water", "juice", "milk", "shake")
print(drinks.index("coffee"))
print(drinks.index("milk", 1))
print(drinks.index("milk", 3, 8))


# sorted
odd_numbers = (24, 9, 3, 15, 18, 6, 27, 12 , 21)
print(sorted(odd_numbers))


pets = ("NezukoMeowMeow", "Waks", "Willow")
print(sorted(pets, key = len))
print(sorted(pets, reverse = True))
