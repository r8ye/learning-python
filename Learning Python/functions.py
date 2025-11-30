name = input("What is your name? ")
print(f"Hi, {name}")

age = input("How old are you? ")
print(f"You are {age} years old.")

food = input("What is your favorite food? ")
print(f"You like {food}.")


# convert to int
print(int(1.000002))
print(int(-12.0))
print(int("67"))
print(int(True))
print(int(False))


# custom functions
def cat():
    print("Hello nezuko")

cat()

def colors():
    color = input("What is your fave color? ")
    print(f"You like {color}")

colors()

def personal_info():
    first_name = input("Ur first name: ")
    last_name = input("Ur last name: ")
    print(f"Fullname: {first_name} {last_name}")

    program = input("Ur program: ")
    print(f"Program: {program}")

    school = input("Ur school: ")
    print(f"School: {school}")

personal_info()


# numbers
def calcu(a, b):
    print(a + b)

calcu(2, 5)


def multiply(a, b):
    print(a * b)

multiply(0, 8)


def subtract(a, b): # best practice
    return a - b

diff = subtract(1, 7)
print(diff)


def division(a, b):
    return a / b

ans_1 = division(12, 6)
ans_2 = division(4, 5)
ans_3 = division(0, 2)

print(ans_1)
print(ans_2)
print(ans_3)


# function with calculations
def calculation(a, b):
    return a / b

num1 = float(input("NUm1: "))
num2 = float(input("Num2: "))
answer = calculation(num1, num2)
print(answer)
