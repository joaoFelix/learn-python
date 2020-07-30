numbers = [1, 5, 3, 6, 2]
largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num

print(f'Largest: {largest}')
