string = "Hello World"

vowels = 'aeoiuAEIOU'

vowel_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"Checking '{string}' for vowels and consonants...")
print(f"There are {vowel_count} vowels and {consonant_count} consonants.")

