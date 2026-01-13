# problem 1
s = "computerxscience"

for subject in s:
    if subject == "x":
        break
    print(subject)


# problem 2
categories = ["fruit", "vegetable"]
items = ["apple", "carrot"]

for category in categories:
    for item in items:
        print(category, item)


# problem 3
words = ["math", "rhythm", "science"]

for word in words:
    found = False
    for i in range(len(word)):
        letter = word[i]
        if letter.lower() in "aeiou":
            print(i)
            found = True
            break
    if not found:
        print(-1)
