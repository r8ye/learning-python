# int_and_float.py

# problem 1
item_1 = 12.75
item_2 = 9.99
item_3 = 5
discount = 0.08
tax = 0.125
person = 3
mod = 7

total_price = round((item_1 + item_2 + item_3), 2)
discounted_price = round((total_price - (total_price * discount)), 2)
taxed = round((discounted_price + (discounted_price * tax)), 2)
floor_div = taxed // person
modulo = round((taxed % mod), 2)

print(f"Total: {total_price}, Discounted: {discounted_price}, Taxed: {taxed}, Floor Division: {floor_div}, Modulo: {modulo}, Type of Total: {type(taxed)}")


# problem  2
int_x = 7
float_y = -2.5

addition = int_x + float_y
subtraction = int_x - float_y
multiplication = int_x * float_y
division = int_x / float_y
floordiv = int_x // float_y
x_raised_y = float(pow(int_x, float_y))
pow_mod = pow(int_x, 3, 5)
round_div = round(division, 1)
convert_div = int(division)

print(f"Sum: {addition}, Difference: {subtraction}, Product: {multiplication}, Division: {division}, Floor Division: {floordiv}, Power x^y: {x_raised_y}, Modular Pow: {pow_mod}, Rounded Division: {round_div}, Converted Int: {convert_div}")

# problem 3

# temp in celsius
t1 = -7.5
t2 = 23
t3 = 0

# celsius to fahrenheit
f1 = (t1 * 9/5 + 32)
f2 = (t2 * 9/5 + 32)
f3 = (t3 * 9/5 + 32)

avg_f = round((f1 + f2 + f3) / 3, 2)

t2_sum_t1 = t2 + t1
t2_diff_t1 = t2 - t1
t2_prod_t1 = t2 * t1
t2_mod_t1 = t2 % t1

floordiv_t2_t3 = t2 // (t3 + 1)

round_avg = round(avg_f, 2)

convert_avg = int(avg_f)

print(f"Fahrenheit: {f1}, {f2}, {f3}, Avg: {avg_f}, Sum: {t2_sum_t1}, Difference: {t2_diff_t1}, Product: {t2_prod_t1}, Modulo: {t2_mod_t1}, Floor Division: {floordiv_t2_t3}, Rounded Avg: {round_avg}, Int Avg: {convert_avg}")



















