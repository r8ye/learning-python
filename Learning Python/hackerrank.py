# n = int(input("Num:" ))
#
# for i in range(n):
#     print(i ** 2)
    

def swap_case(s):
    return s.swapcase()

res = swap_case("pypy 3")
print(res)



def fizzBuzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return n

print(fizzBuzz(10))


def reverse_words_order_and_swap_cases(sentence):
    reverse_words = " ".join(sentence.split()[::-1])
    swap_cases = reverse_words.swapcase()
    return swap_cases


reverse_words_order_and_swap_cases("aWESOME is cODING")


for i in range(1, 11):
    print(f"Hello World {i}")





