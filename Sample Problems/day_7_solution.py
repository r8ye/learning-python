# scope.py

# problem 1
def mystery():
    txt = "outer"

    def change():
        nonlocal txt
        txt = "modified inner"
        print(txt)

        txt = "modified outer"
        print(txt)
    change()

mystery()


# problem 2
value = "GLOBAL"

def test():
    value = "LOCAL"

    def inner():
        global value
        print(value)

    inner()
    print(value)

print(value)
test()
print(value)


# problem 3
password = "root"

def system():
    password = "admin"

    def reset():
        global password
        password = "admin"
        print(password)

    reset()
    print(password)

print(password)
system()
print(password)