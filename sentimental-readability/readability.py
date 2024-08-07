# TODO

# Simple one line user input
Text = input("Text: ")

letters = sentences = words = 0

# Checks the Sentences and Words that is typed in
for char in Text:
    if char.isalpha():
        letters += 1
    elif char.isspace():
        words += 1
    elif char in ['?', '.', '!']:
        sentences += 1

# Variables used
words += 1
L = (letters * 100.0) / words
S = (sentences * 100.0) / words

# Equation used from C programming implemented in Python to determine Grade level
result = int((0.0588 * L - 0.296 * S - 15.8) + 0.5)
if result < 1:
    print("Before Grade 1")
elif result >= 16:
    print("Grade 16+")
else:
    print(f"Grade {result}")