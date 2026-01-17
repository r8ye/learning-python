# using def function
from traceback import print_tb

numbers = [1,2 , 3, 4, 5]

def list_even_numbers(x):
    return x % 2 == 0

even_numbers = list(filter(list_even_numbers, numbers))
print(even_numbers)


# using lambda function
odd_numbers = [1, 3, 5, 7, 9, 11]

greater_than_5 = list(filter(lambda odd: odd > 5, odd_numbers))
print(greater_than_5)


list_numbers = [65, 79, 80, 93]

multiples_five = list(filter(lambda num: num % 5 == 0, list_numbers))
print(multiples_five)
