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

power = pow(num1, num4)
print("Power:", power)

print(int(num2))
print(float(num1))
print(round(num2))
print(abs(num3))
print(bin(num1))
print(oct(num3))
print(hex(num1))


# Augmented Assignments
addition = 3
addition += 8
print(addition)

floor_division = 69
floor_division //= 7
print(floor_division)

modulu = 100
modulu %= 11
print(modulu)


# Functions
def add(a, b):
    return a + b

sum1 = add(6, 7)
print(sum1)


def exp(a, b):
    return a ** b

ans = exp(2, 3)
print(ans)


float1 = 4.5
float2 = 8.2

def solve(a, b):
    return a / b

answer = solve(float1, float2)
print(answer)


# firstname = input("What is your first name? ")
# lastname = input("What is your lastname? ")
# combine = f"Hello {firstname} {lastname}! Nice to meet you."
# print(combine)


def local_scope():
    num5 = 88
    print(num5)


def outer_function():
    enclosing = "Enclosing Scope"

    def inner_function():
        print(enclosing)
    inner_function()

outer_function()



tax = 0.70

def get_total(subtotal):
    total = subtotal + (subtotal * tax)
    return total

print(get_total(100))


tax_rate = 0.2

def calculate(price):
    return price - (price * tax_rate)

print(calculate(1000))


apple = 20
grapes = 400
egg = 10

def calculate3():
    return (apple * 5) + (grapes / 4) + (egg * 12)

print(calculate3())


# input1 = int(input("Enter num1: "))
# input2 = int(input("Enter num2: "))
#
# def calculate4():
#     return input1 % input2
#
# print("Answer: ", calculate4())


# Comparison Operators
print(5 == 5)
print(7 > 8)
print(2.5 <= 2)
































