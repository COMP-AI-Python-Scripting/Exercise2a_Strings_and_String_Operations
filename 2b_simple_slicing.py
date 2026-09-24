name = "jonathon"

print(f"Original string name is {name}")

first_character = name[0]
last_character = name[-1]

name_length = len(name)

middle_character_index = int(name_length/2)
middle_character = name[middle_character_index]

abbreviated_name = first_character + middle_character + last_character

print(f"Abbreviated form of name {name} is {abbreviated_name}")


