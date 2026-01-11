# problem 1
prog_lang = ["Python", "C++", "Rust"]

prog_lang[-1] = "JavaScript"
prog_lang.insert(1, "Go")
prog_lang.remove("Python")
prog_lang.reverse()

print(prog_lang)
print(prog_lang.index("JavaScript"))
print("Rust" in prog_lang)

# problem 2
data = ["Rachelle", 21, "CCS", [1.67, "hello", "world"]]

extracted_data = data[3]
name, age, dept, *rest = data

print(extracted_data)
print(extracted_data[1])
print(name)
print(age)
print(dept)
print(list(name))
print(rest)


# problem 3
items = ["a", "b", "c"]
extras = ["x", "y"]
nums = [1, 2, 3, 4, 5]

items.append(extras)
items.insert(2, "z")
items.remove("b")
nums.pop()

print(items)
print(nums)
print(nums[1::2])
