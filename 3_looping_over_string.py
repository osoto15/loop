# Example Practice:
# Ask the user for a word.
word = input("Provide a word: ")

# Use a for loop to print each letter on a new line.
for letter in word:
    print(letter)

# Challenge:
# Count how many vowels are in the word.
vowels = "aeiouAEIOU"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print("numbers of vowels,", count)
