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
