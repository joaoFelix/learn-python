numbers_dictionary = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

numbers = input("Numbers: ")

translation = f'{numbers_dictionary.get(numbers[0])}'

for num in numbers[1:]:
    translation += f' {numbers_dictionary.get(num)}'

print(translation)

