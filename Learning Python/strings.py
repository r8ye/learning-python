string_1 = "Hello"
print(string_1)

string_2 = """multiline
string"""
print(string_2)

string_3 = """isa 
pang
multi
line"""
print(string_3)


# concatenation
msg = "okay'ed"
quote: str = 'she said, "hello earth"'
print(msg, quote)

msg_plus_quote = msg + " " + quote
print(msg_plus_quote)

print(f"{msg} {quote}") # most acceptable

name = "Rachelle Fraga"
program = "BSCS"
year = 3
print(f"My name is {name}. I am a {year}rd year {program} student.") # most acceptable

program_plus_year = program + str(year)
print(program_plus_year)

cat_name = "Nezuko"
cat_age = 1
cat_name_plus_age = f"My cat's name is {cat_name}. She is {cat_age} years old"
print(cat_name_plus_age)

num_1 = 6
num_2 = 7
print(f"the sum of {num_1} and {num_2} is {num_1 + num_2}")

# indexing
string_length = "hello nezuko"
print(len(string_length))
print(string_length[0])
print(string_length[5])
print(string_length[8])
print(string_length[-1])
print(len(string_length[6]))


# string slicing string[start:stop]
string_hbd = "Happy birthday!"
print(string_hbd[2:10]) # ppy birt
print(string_hbd[4:5]) # y
print(string_hbd[4:6]) # y
print(string_hbd[:9]) # Happy bir
print(string_hbd[7:]) # irthday!
print(string_hbd[:]) # Happy birthday!
print(string_hbd[0:99]) # Happy birthday!

# string[start:stop:step}
xmas = "Merry Christmas!"
print(xmas[1:11:3]) # eyhs
print(xmas[5:16:2]) #  hita!

# reverse a string
word = "happy"
print(word[::-1]) # yppah
print(word[1::-1]) # ah
print(word[2::-1]) # pah
print(word[4:2:-1]) # yp


# in operator
greetings = "merry xmas and happy new year"
print("merrys" in greetings)
print("mer" in greetings)
print("z" in greetings)
print("" in greetings)
print(" w" in greetings)
print("w " in greetings)

ccs = """college
of
computer
studies"""
print(ccs)
print("compiter" in ccs)
print(ccs[8:14])
print(ccs[3:20:4]) # cu
print(ccs[::-1])
print("\n" in ccs)
print(ccs[18:7:-1])
