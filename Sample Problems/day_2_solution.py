# strings.py

# problem 1
student_name = "Alex Rodriguez"
major = "Electronics Engineering"
id_number = 202312345
print(f"""Student Profile""")
print(f"""Profile: {student_name} - Major: {major} - ID: {id_number}""")

# problem 2
quote_phrase = "Coding is fun and useful for everyone!"
print(quote_phrase[0])
print(quote_phrase[18])
print(quote_phrase[10:24])
print(quote_phrase[::-1])

# problem 3
sentence = "The quick brown fox jumps over the lazy dog."
secret_word = "ox j"

is_present: bool = secret_word in sentence
action_word: str = sentence[20:25]
print(f"The word we found is: {action_word}. Is the secret word part of the sentence? {is_present}.")
