# local scope
def my_function():
    my_variable = 10
    print(my_variable)

my_function()


def fill():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    age = input("How old are you? ")

    print(f"My name is {first_name} {last_name}. I am {age} years old.")
fill()


# enclosing scope
def my_outer_function():
    msg = "Zodiac killer"

    def my_inner_function():
        print(msg)

    my_inner_function()

my_outer_function()


def calculate():
    x = -8
    y = 12

    def addition(a, b):
        return a + b

    ans = addition(x, y)
    print(ans)

    def subtraction(a, b):
        return a - b

    ans_2 = subtraction(x, y)
    print(ans_2)

calculate()


def outer_space():
    a = "Aliens"
    b = ""

    def earth():
        nonlocal b
        b = "Humans"
        print(b)
        print(a)

    earth()

outer_space()


# global scope
global_variable = 1000

def global_scope():
    print(global_variable)

global_scope()
print(global_variable)

global_a = "Global Warming"

def global_scope_example():
    global global_b
    global_b = "Global Economy"
    print(global_a)
    print(global_b)

global_scope_example()
print(global_b)


current_pass = 12345

def change_pass():
    global current_pass
    current_pass = 6969
    print(current_pass)

change_pass()


# built-in function
print(str(534))
print(type(123))
print(type(12.0))
print(type("hey"))
print(isinstance("haha", int))



























