full_name = "kurt friedrich godel"

names = full_name.split()
name_elements = ['First', 'Middle', 'Last']

for name, element in zip(names, name_elements):
    print(f"{element}: {name.title()}")


