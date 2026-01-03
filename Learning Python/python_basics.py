print("hello world")

my_int = 100
print("Integer:", my_int)

my_float = 2.5
print("Float:", my_float)

my_str = "love"
print("String:", my_str)

my_bool = False
print("Boolean:", my_bool)

my_set = {1, 2, 3}
print("Set:", my_set)

my_dictionary = {"name": "Rachelle", "age": 21}
print("Dictionary", my_dictionary)

my_tuple = (5, 4, 3)
print("Tuple:", my_tuple)

my_range = range(8)
print("Range:", my_range)

my_none = None
print("None:", my_none)

my_list = [5, "cs", 4.66, True]
print("List", my_list)


# immutable and mutable types

#type
pangalan = "Rachelle"
edad = 21

print(type(edad))
print(type(pangalan))

# isinstance
print(isinstance(pangalan, str))
print(isinstance(edad, float))

# Accessing Characters from Strings
word = "computer science"

print(word[0])
print(word[8])
print(word[11])


# f-strings
sentence = f"My name is {pangalan}."
print(sentence)
print(f"I am {edad} years old.")

# String Slicing
msg = "I love nanay!"

print(msg[0:])
print(msg[2:6])
print(msg[2:12:3])

# length
print(len(msg))

# in operator
print("tatay" in msg)
print("love" in msg)


# string methods
it = "   Information Technology   "

print(it.upper())
print(it.lower())
print(it.strip()) # trim
print(it.replace("Technology", "Systems"))
print(it.split(" "))
print(it.find("Science"))
print(it.find("Information"))
print(it.count("i"))
print(it.count("o"))
print(it.capitalize())
print(it.islower())


listahan = ["apple", "mango", "strawberry"]
join_listahan = " ".join(listahan)
print(join_listahan)


trans_table = str.maketrans("xyz", "321")
print(trans_table)

result = "zyx".translate(trans_table)
print(result)


# Basic Math Operations
num1 = 12
num2 = 5.5
num3 = -67
num4 = 4

sum = num1 + num2
print("Sum:", sum)

difference = num1 - num2
print("Difference:", difference)

product = num1 * num2
print("Product:", product)

quotient = num1 / num2
print("Quotient:", quotient)

modulus = num1 % num2
print("Modulo:", modulus)

floor_div = num1 // num2
print("Floor Division:", floor_div)

exponent = num1 ** num2
print("Exponent:", exponent)

print(int(num2))
print(float(num1))
print(round(num2))
print(abs(num3))
print(bin(num1))
print(oct(num3))
print(hex(num1))

power = pow(num1, num4)
print("Power:", power)

























