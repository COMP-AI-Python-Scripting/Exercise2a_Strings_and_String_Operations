integers = [1,2,3]
numbers=['one', 'two', 'three']

for i in integers:
    print(i)

for number in numbers:
    print(number)

for i, number in zip(integers, numbers):
    print(f"{i}: {number}")
