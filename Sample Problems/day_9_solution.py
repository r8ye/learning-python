# problem 1
age = int(input("Age: "))
citizen = input("yes or no? ")
education = input("Education? ")

strip_lower_citizen = citizen.strip().lower()
strip_lower_educ = education.strip().lower()

if age >= 18 and strip_lower_citizen == "yes" and (strip_lower_educ == "bachelor" or "masters" or "phd"):
    print("Qualified")
else:
    print("Not qualified")


# problem 2














