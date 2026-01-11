prog_lang = ["Python", "C++", "Rust"]
prog_lang[-1] = "Javascript"
print(prog_lang)

dev = "Rachelle"
print(list(dev))

names = ["Nazz", "Jess", "Angelo"]
del names[0]
print(names)
print("Jade" in names)


sample = [1, True, "ccs", [1.67, "hello", "world"]]
print(sample[3])
print(sample[3][1])


info = ["Rachelle Fraga", 21, "CCS"]
name, age, dept = info
print(name)
print(age)
print(dept)

pets = ["nezuko", "cheeto", "wakin", "willow"]
pets_name, *rest = pets
print(pets_name)
print(rest)


colors = ["red", "yellow", "green", "blue", "purple"]
print(colors[2:5])
print(colors[0:4:2])

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[3::3])
print(sorted(nums))


# append
numbers = [2, 4, 6, 8, 10]
print(numbers)

pagkain = ["barbeque", "cheese", "lobster"]
additional_food = ["bacon", "avocado", "pizza"]

pagkain.append(additional_food)
print(pagkain)


# extend
kulay = ["red", "blue", "yellow"]
add_kulay = ["purple", "garnet", "pink"]

kulay.extend(add_kulay)
print(kulay)


# insert
letters = ["a", "b", "c", "d"]
letters.insert(3, "z")

print(letters)


# remove
vowels = ["a", "e", "i", "o", "u"]
vowels.remove("o")

print(vowels)

consonants = ["b", "c", "d", "f", "f", "f"]
consonants.remove("f")

print(consonants)


# pop
numero = [1, 2, 3, 4, 5]
numero.pop()

print(numero)


# clear
programs = ["cs", "it", "ece"]
programs.clear()

print(programs)


# sorted
nums = [8, 5, 2, 9, 5, 1]
print(sorted(nums))


# reverse
nums_2 = [9, 8, 7, 6, 5]
nums_2.reverse()

print(nums_2)


# index
languages = ["english", "japanese", "korean", "filipino"]
print(languages.index("korean"))
