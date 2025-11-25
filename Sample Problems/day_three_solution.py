# string_methods.py

# problem 1
birthday_message = "happy birthday friend"
upper_birthday = birthday_message.upper()
print(upper_birthday)

holiday_message = "MERRY CHRISTMAS AND A HAPPY NEW YEAR"
lower_holiday = holiday_message.lower()
print(lower_holiday)

story = "once upon a time in coding land"
title_story = story.title()
print(title_story)


# problem 2
messy_text = "   hello python world   "
clean_text = messy_text.strip()
print(clean_text)

statement = "i love programming"
new_statement = statement.replace("love", "enjoy")
print(new_statement)

fruits = ["banana", "apple", "grapes"]
joined_fruits = "-".join(fruits)
print(joined_fruits)


# problem 3
quote = "winds carry memories of you"
first_space_index = quote.find(" ")
print(first_space_index)

count_r = quote.count("r")
print(count_r)

str_1 = "HELLO WORLD"
check_upper = str_1.isupper()
print(check_upper)

str_2 = "introduction"
check_lower = str_2.islower()
print(check_lower)

filename = "notes.txt"
is_text_file = filename.endswith(".txt")
print(is_text_file)



















