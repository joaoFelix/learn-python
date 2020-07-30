names = ['Joao', 'Felix', 'Keity', 'Ribeiro']

print(names[-1]) # Last item = Ribeiro
print(names[2:]) # names from 3rd until the last
print(names[:2]) # names from 2nd (idx-1) until the 3rd

numbers = [5, 2, 1, 7, 4]

numbers.insert(0, 20) # insert 20 at index 0

print(numbers.pop()) # Print last item in list
print(50 in numbers) # Check if 50 exists in the list