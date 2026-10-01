fullname = 'kurt godel'

middlename = 'friedrich'

firstname, lastname = fullname.split()

newfullname = ' '.join((firstname, middlename, lastname)).title()

print(f"Original fullname: {fullname}")
print(f"Middle name: {middlename}")
print(f"Firstname: {firstname}")
print(f"Lastname: {lastname}")
print(f"New fullname: {newfullname}")

