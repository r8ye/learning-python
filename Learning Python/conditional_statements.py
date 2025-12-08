print(8 == 9)
print(1 > 2)
print ( 67 != 67)
print(5 >= 6)
print(5  <= 7)


# if statements
age = 89

if age >= 60:
    print("ang tanda mo na")


# if-else statements
age = 8

if age >= 18:
    print("adult")
else:
    print("kid")


score = 94

if score >= 75:
    print("you passed")
else:
    print("you failed")




# elif
marks = 88

if marks >= 90:
    print("Outstanding")
elif marks >= 80:
    print("Excellent")
elif marks >= 75:
    print("pasang awa")
else:
    print("u failed")


# and
is_alive = True
num = 12

print(is_alive and num)


is_citizen = True
edad = 17

if is_citizen and edad >= 18:
    print("mag trabaho ka na")
elif is_citizen and age < 18:
    print("bawal minor pa")
else:
    print("di pwede")


# or
is_bachelors = False
is_masters = False
is_phd = True

if is_bachelors or is_masters or is_phd:
    print("100% qualified")
else:
    print("disqualified")


# not
is_admin = True

if not is_admin:
    print("access denied")
else:
    print("successful")


# and, or, not
exp = 5
is_filipino = True
is_graduate = False
is_alien = False

if exp >= 3 and not is_alien and (is_filipino or is_graduate):
    print("eligible")
else:
    print("uneligible")
