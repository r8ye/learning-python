lang = ["python", "c++", "java"]
index = 0

for language in lang:
    print(f"index {index} and language {lang}")
    index += 1


# enumerate
languages = ["English", "Filipino", "Japanese"]

print(list(enumerate(languages)))


games = ["valorant", "codm", "supersus", "league", "dota"]

for ind, game in enumerate(games):
    print(f"Index: {ind} and Game: {game}")


letters = ["a", "b", "c", "d"]

for ind_2, letter in enumerate(letters, 2):
    print(f"Index: {ind_2} and Letter: {letter}")


# zip
pets = ["nezuko", "willow", "wakin"]
age = [1, 2, 3]

print(list(zip(pets, age)))

for pet, yo in zip(pets, age):
    print(f"Pet name: {pet}")
    print(f"Age: {yo}")


devs = ["linus", "mark", "steve"]
ids = [3, 2, 1]

for dev, id in zip(devs, ids):
    print(f"Dev: {dev}")
    print(f"ID: {id}")
