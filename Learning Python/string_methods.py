# uppercase
hbd = "happy birthday!"
upper_hbd = hbd.upper()
print(upper_hbd)

ily = """i
love
you"""
upper_ily = ily.upper()
print(upper_ily)


# lowercase
xmas = "Merry Christmas"
lower_xmas = xmas.lower()
print(lower_xmas)

nye = """HAPPY
NEW
YEAR"""
lower_nye = nye.lower()
print(lower_nye)


# trim - beginning and end lang na whitespace
hello = "hello world   "
trim_hello = hello.strip()
print(trim_hello)

# invalid trimming
cat = """             nezuko          
        meow      
                meow"""
trim_cat = cat.strip()
print(trim_cat)


# replace
pypy = "python project"
replace_pypy = pypy.replace("python", "c++")
print(replace_pypy)

water = "nature's spring"
replace_water = water.replace("nature", "sky")
print(replace_water)


# join
my_list = ["apple", "strawberry", "mango"]
join_my_list = " ".join(my_list)
print(join_my_list)

list_subjects = ["Math", "sciEnce", "englisH"]
join_list_subjects = " ".join(list_subjects)
print(join_list_subjects)


# starts with
numbers = "1, 2, 3, 4, 5"
start_numbers = numbers.startswith("2")
print(start_numbers)


# ends with
letters = "a, b, c, d"
end_letters = letters.endswith("z")
print(end_letters)


# find(substring) index
phrase = "i love programming"
find_phrase = phrase.find(" ")
print(find_phrase)

find_phrase_2 = phrase.find("python")
print(find_phrase_2)

find_phrase_3 = phrase.find("programming")
print(find_phrase_3)


# count(substring) case sensitive
sentence = "Winds carry memories of you."
count_w = sentence.count("w")
print(count_w)

count_space = sentence.count(" ")
print(count_space)

count_m = sentence.count("m")
print(count_m)


# capitalize
string = "dreams bloom where hope lingers."
capitalize_string = string.capitalize()
print(capitalize_string)

string_2 = "sssoft rain heals the restless heart."
capitalize_string_2 = string_2.capitalize()
print(capitalize_string_2)


# isupper all the letters
string_3 = "Stars whisper secrets at midnight."
isupper_string_3 = string_3.isupper()
print(isupper_string_3)

string_4 = "HELLO WORLD"
isupper_string_4 = string_4.isupper()
print(isupper_string_4)


# islower all the letters
intro = "introduction"
islower_intro = intro.islower()
print(islower_intro)


# title
project = "python project"
title_project = project.title()
print(title_project)

ide = "VISUAL STUDIO CODE"
title_ide = ide.title()
print(title_ide)
