firstname = 'joe'
middlename = 'john'
lastname = 'bloggs'

print("Individual String Variables:")
print(f"firstname = {firstname}")
print(f"middlename = {middlename}")
print(f"lastname = {lastname}\n")

fullname1 = firstname + middlename + lastname
print(f"Concatenated Full Name: {fullname1}, an error!\n")


fullname2 = firstname + ' ' + middlename + ' ' + lastname
print(f"Concatenated Full Name: {fullname2}, a little better.\n")


fullname3 = f"{firstname.capitalize()} {middlename.capitalize()} {lastname.capitalize()}"
print(f"Formatted String Full Name: {fullname3}, much better.\n")


fullname4 = f"{firstname.capitalize()} {middlename[0].capitalize()}. {lastname.capitalize()}"
print(f"Formatted String Formal Name: {fullname4}, capitalised and abbreviated middle\
name.\n")
