even_num = []

for num in range(21):
    if num % 2 == 0:
        even_num.append(num)

print(even_num)


# [value for item in iterable if condition]
odd_num = [odd for odd in range(12) if odd % 2 != 0]
print(odd_num)


even_num2 = [even for even in range(2, 15) if even % 2 == 0]
print(even_num2)


# [APPEND_VALUE if CONDITION else OTHER_VALUE for ITEM in ITERABLE]
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [(number, "Odd Number") if number % 2 != 0 else (number, "Even Number") for number in list_num]
print(res)


list_items = [0, True, -1, False, None, "Computer", " ", ""]

true_or_false = [(item, "True") if bool(item) == True else (item, "False") for item in list_items]
print(true_or_false)


# filter
words = ["computer", "cs", "science", "math", "python"]

def is_short_word(word):
    return len(word) < 5

short_words = list(filter(is_short_word, words))
print(short_words)


phrases = ["i love phyton", "i hate jave", "i am programming", "free code camp"]

def is_long_phrase(phrase):
    return len(phrase) > 15

long_phrase = list(filter(is_long_phrase, phrases))
print(long_phrase)


# map
celsius = [15, 30, 45, 60, 75, 100]

def to_fahrenheit(temperature):
    return (temperature * 9/5) + 32

fahrenheit = tuple(map(to_fahrenheit, celsius))
print(fahrenheit)


def calculate(n):
    return n / 2

nums = [9, 8, 7, 6, 5]
ans = list(map(calculate, nums))
print(ans)


# sum
list_numbers = [10, 15, 20, 25, 30]
total = sum(list_numbers)
print(total)


another_list = [4, 8, 12, 16]
total_another_list = sum(another_list, 6.7)
print(total_another_list)
