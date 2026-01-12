# # for loop: Python stops after the last character/item
# prog_langs = ["C++", "Python", "C#"]
#
# for language in prog_langs:
#     print(language)
#
#
# food = ["spaghetti", "pasta", "pizza"]
#
# for x in food:
#     print(x)
#
#
# for letters in "code":
#     print(letters)
#
#
# for char in "computer science":
#     print(char)
#
#
# week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#
# for day in week:
#     print(day)
#
#
# # for loops: For every category, list every food
# categories = ["fruit", "vegetable"]
# foods = ["mango", "grapes", "cabbage", "carrots"]
#
# for category in categories:
#     for food in foods:
#         print(category, food)


# # while loop: Stops only when the condition becomes False
# num = 0
#
# while num <= 5:
#     print(num)
#     num += 1
#
#
# secret_num = 7
# guess = 1
#
# while guess != secret_num:
#     guess = int(input("Find the secret number (1-10): "))
#     if guess != secret_num:
#         print("Try again.")
#
# print("Correct!")


# break
vowels = ["a", "e", "i", "o", "u"]

for letter in vowels:
    if letter == "u":
        break
    print(letter)


# continue
even_numbers = [2, 4, 6, 8, 10]

for num in even_numbers:
    if num == 6:
        continue
    print(num)




# aralin pa to
subjects = ["math", "science", "english", "filipino", "xzy"]

for subject in subjects:
    for char in subject:
        if char.lower() in "aeiou":
            print(f"{subject} has letter {char}")
            break
    else:
        print(f"{subject} has no vowel")
