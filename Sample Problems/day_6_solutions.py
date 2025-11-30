# functions.py

# problem 1
def greet_user():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    print(f"Hello, {first_name} {last_name}!")

greet_user()


# problem 2
def add(a, b):
    return a + b

num_1 = int(input("Num 1: "))
num_2 = int(input("Num 2: "))
get_sum = add(num_1, num_2)
print(f"Sum: {get_sum}")


def subtract(a, b):
    return a - b

num_3 = int(input("Num 1: "))
num_4 = int(input("Num 2: "))
get_diff = subtract(num_3, num_4)
print(f"Difference: {get_diff}")


def multiply(a, b):
    return a * b

num_5 = int(input("Num 1: "))
num_6 = int(input("Num 2: "))
get_product = multiply(num_5, num_6)
print(f"Product: {get_product}")


def division(a, b):
    return a / b

num_7 = int(input("Num 1: "))
num_8 = int(input("Num 2: "))
get_quotient = division(num_7, num_8)
print(f"Quotient: {get_quotient}")


# problem 3
def favorite_things():
    fav_food = input("Fav food: ")
    fav_color = input("Fav color: ")
    fav_num = int(input("Fav number: "))

    print(f"You like {fav_food}.")
    print(f"Your favorite color is {fav_color}.")
    print(f"Your favorite number is {fav_num}.")

favorite_things()
