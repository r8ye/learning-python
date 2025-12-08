# conditional_statements.py

# problem 1
age = 18
is_citizen = True
has_valid_id = True

if age >= 18 and is_citizen and has_valid_id:
    print("allowed to vote")
else:
    print("not allowed")


# problem 2
score = 60
is_athlete = True
is_banned = False

if score >= 85 and not is_banned:
    print("qualified")
elif score >= 75 and is_athlete and not is_banned:
    print("qualified")
else:
    print("not qualified")


# problem 3
exp = 5
has_degree = False
has_certificate = True
is_foreign = False

if exp >= 2 and (has_degree or has_certificate) and not is_foreign:
    print("accepted")
else:
    print("rejected")












