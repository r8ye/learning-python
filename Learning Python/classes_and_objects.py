class Cats:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"Name: {self.name}. Age: {self.age}")

cat1 = Cats("Nezuko", 1)
cat2 = Cats("Akira", 0)

cat1.meow()
cat2.meow()


class Friends:
    def __init__(self, fullname, program, year):
        self.fullname = fullname
        self.program = program
        self.year = year

    def info(self):
        print(f"{self.fullname} is a {self.year} college student. Currently taking {self.program} at TFVC.")

friend1 = Friends("Angelo", "BSIT", "3rd")
friend2 = Friends("Jess", "BSCS", "3rd")

friend1.info()
friend2.info()


# Handle Object Attributes Dynamically

# getattr
class Tao:
    def __init__(self, birthday, nickname):
        self.birthday = birthday
        self.nickname = nickname

tao = Tao("Aug 26", "Raye")

print(getattr(tao, "birthday"))
print(getattr(tao, "nickname"))
print(getattr(tao, "hometown", "paracale"))


class ShowGrades:
    def __init__(self, subject, gwa):
        self.subject = subject
        self.gwa = gwa

subject = ShowGrades("math", 1.5)

attr_subj = input("enter attribute: ")
print(getattr(subject, attr_subj, "no grades available"))


# dir
class Language:
    def __init__(self, lang, country):
        self.lang = lang
        self.country = country

language = Language("filipino", "philippines")

for attr in dir(language):
    if not attr.startswith("__") and not callable(getattr(language, attr)):
        value = getattr(language, attr)
        print(f"{attr}: {value}")