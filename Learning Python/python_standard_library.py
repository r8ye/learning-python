import math
print(math.sqrt(64))
print(math.pi)



import datetime
current_date = datetime.date(2026, 1, 23)

print(current_date.year)
print(current_date.month)
print(current_date.day)


bday = datetime.date(2004, 8, 26)
print(bday.day)


# assigning an alias
import math as m
print(m.sqrt(36))


# not importing the whole library
from math import radians
angle = 40
angle_radian = radians(angle)
print(angle_radian)



from math import radians as rad, sin as s, cos as c
degree_angle = 60

angle_rad = rad(degree_angle)
print(angle_rad)

angle_sin = s(angle_rad)
print(angle_sin)

angle_cosine = c(angle_rad)
print(angle_cosine)



# if __name__ == "__main__":