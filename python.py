# print
print("hello world")
print("my favorite food are", "shawarma", "chicken", "sinigang")


# data types
positive_integer = 69
negative_integer = -67
print("Integer:", negative_integer)

positive_float = 6.9
negative_float = -9.69
print("Float:", positive_float)

complex_var = 4 - 5j
print("Complex:", complex_var)

string_first_name = "Rachelle"
string_last_name = "Fraga"
print("String:", string_first_name, string_last_name)

boolean_true = True
boolean_false = False
print("Boolean:", boolean_false)

set_var = {0, 1, 2, 3}
print("Set:", set_var)

dictionary_var = {"name": "nezuko meow meow", "age": 5}
print("Dictionary:", dictionary_var)

tuple_random = ("Meow", 67, 3.4)
tuple_integers = (2, 3, -1)
print("Tuple:", tuple_random, "and", tuple_integers)

range_y = range(1)
range_xy = range(2, 5)
print("Range:", range_y, "and", range_xy)

my_list = [214, "am i real", -6.9, False]
print("List:", my_list)

none_var = None
print("None:", none_var)


# strings are immutable
# mutable examples:
list_of_num = [5, 4, 3, 2, 1, 0]
list_of_num[1] = 696969
print(list_of_num) # replacing the variable

var_one = {1, 2, 3}
var_two = -0.1
var_three = True
var_four = "Meow"
var_five = None
print(type(var_five)) # getting the data type


# datatypes + their types
none_variable = None
list_variable = ["okay'ed", 666, -0.1, True]
range_variable = range(0, 10)
tuple_variable = (1, -2, "Me", 0.4)
dictionary_variable = {"title": 1251, "genre": "love song"}
set_variable = {0, 1, 2, 3, 4, 5}
bool_variable = True
string_variable = "python"
complex_variable = 3 + 14j
float_variable = -6.9000
integer_variable = 67

print("Integer:", integer_variable, "| Type:", type(integer_variable))
print("Float:", float_variable, "| TYpe:", type(float_variable))
print("Complex:", complex_variable, "| Type:", type(complex_variable))
print("String:", string_variable, "| Type:", type(string_variable))


# hints
cat: str = "Meow"
print(cat)


def today(month: str, date: int) -> str:
    return f"Today is {month} {date}!"

month_now: str = "November"
date_now: int = 23

print(today(month_now, date_now))
