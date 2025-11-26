# getting the data type
int_1 = 12
int_2 = -8
print(type(int_1))
print(type(int_2))

float_1 = 9.4354
float_2 = -0.8
print(type(float_1))
print(type(float_2))


# arithmetic operations
# int
int_x = 79
int_y = -9

# add
add_int = int_x + int_y
print(add_int)

# subtract
subtract_int = int_x - int_y
print(subtract_int)

# multiply
multiply_int = int_x * int_y
print(multiply_int)

# divide
divide_int = int_x / int_y
print(divide_int)


int_a = -69
int_b = 67

sum_ab = int_a + int_b
print(sum_ab)  # -2

subtract_ab = int_a - int_b
print(subtract_ab)  # -136

multiply_ab = int_a * int_b
print(multiply_ab) # -4623

divide_ab = int_a / int_b
print(divide_ab)   # -1.02...


# float
float_1 = -95.764
float_2 = 0.67

# add
add_float = float_1 + float_2
print(f"Addition: {add_float}")

# subtract
subtract_float = float_1 - float_2
print(f"Subtraction: {subtract_float}")

# multiply
multiply_float = float_1 * float_2
print(f"Multiplication: {multiply_float}")

# division
divide_float = float_1 / float_2
print(f"Division: {divide_float}")


# int and float
num_1 = 43
num_2 = -6.7

int_plus_float = num_1 + num_2
print(int_plus_float)
print(type(int_plus_float))

int_minus_float = num_1 - num_2
print(int_minus_float)
print(type(int_minus_float))

int_times_float = num_1 * num_2
print(int_times_float)
print(type(int_times_float))

int_divide_float = num_1 / num_2
print(int_divide_float)
print(type(int_divide_float))


# modulo
num_3 = 11
num_4 = 2.5

modulo_num = num_3 % num_4
print(modulo_num)
print(type(modulo_num))


# floor division
num_5 = 89
num_6 = 8
floor_int = num_5 // num_6
print(floor_int)

num_7 = -2.34
num_8 = 1
floor_float = num_7 // num_8
print(floor_float) # round down kaya -3.0


# exponent
num_9 = 2
num_10 = 4
exp_int = num_9 ** num_10
print(exp_int)

num_11 = 8
num_12 = 0.9
exp_float = num_11 ** num_12
print(exp_float)


# convert float/int/strings
num_13 = 6.7
convert_num_13 = int(num_13)
print(convert_num_13)
print(type(convert_num_13))

num_14 = 14
convert_num_14 = float(num_14)
print(convert_num_14)
print(type(convert_num_14))

num_15 = "15"
convert_str_15 = float(num_15)
print(convert_str_15, type(convert_str_15))

num_16 = "1"
convert_str_16 = int(num_16)
print(convert_str_16, type(convert_str_16))

num_17 = "1.99"
convert_str_17 = int(float(num_17))
print(convert_str_17, type(convert_str_17))


# round off
num_18 = 9.9990213
round_off = round(num_18)
round_1 = round(num_18, 1)
round_2 = round(num_18, 2)
round_3 = round(num_18, 3)

print(f"{round_off}, {round_1}, {round_2}, {round_3}")

num_19 = "-0.3867835466357568"
convert_round = round(float(num_19), 7)
print(convert_round)

num_20 = "-202020.92929"
conver_round_2 = round(float(num_20), 4)
print(conver_round_2)


# absolute, binary, octal, hexadecimal
num_21 = -8

absolute_value = abs(num_21)
print(absolute_value)

binary_value = bin(num_21)
print(binary_value)

num_22 = -7
binary = bin(abs(num_22))
print(binary)

octal = oct(num_22)
print(octal)

hexadecimal = hex(num_22)
print(hexadecimal)


# power
num_23 = pow(3, 4)
print(num_23)

num_24 = pow(2, 4, 3)
print(num_24)
