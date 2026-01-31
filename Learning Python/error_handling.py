# error handling
import pdb

def add(x, y):
    pdb.set_trace()
    return x + y

print(add(2, 1))



def multiply(a, b):
    res = a + b
    print(f"multiplying {a} and {b} gives {res}")
    return res

multiply(10, 5)



# exception handling
try:
    c = 5 / 0
except ZeroDivisionError:
    print("cant divide by 0")
else:
    print(f"quotient: {c}")
finally:
    print("running")


try:
    num = int(input("Num: "))
    division = 12 / num
except ValueError:
    print("input should be int")
except ZeroDivisionError:
    print("cant be divided by 0")
else:
    print(f"ans: {division}")
finally:
    print("run")


try:
    input1 = int(input("Num 1: "))
    input2 = int(input("Num 2: "))
    division_2 = input1 / input2
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred at: {e}")





















