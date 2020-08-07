names = ['Joao', 'Felix', 'Keity', 'Ribeiro']

print(names[-1]) # Last item = Ribeiro
print(names[2:]) # names from 3rd until the last
print(names[-2:]) # Last 2 items
print(names[:2]) # names from 0th until the 3rd

numbers = [5, 2, 1, 7, 4]

numbers.insert(0, 20) # insert 20 at index 0

print(numbers.pop()) # Print last item in list
print(50 in numbers) # Check if 50 exists in the list

numbers.append(10)  # append to the end of the list

print(numbers.index(7, 1))  # The index of 7 starting from the index 1 on the list (ignoring index 0)

print(numbers.__getitem__(0))  # same as numbers[0]

numbers.clear()

