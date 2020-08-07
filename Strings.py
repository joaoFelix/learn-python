first = 'Joao'
last = 'Felix'

message = first + ' [' + last + '] is a coder'

msg = "%s %s is a coder" % (first, last)

print(msg)

# Formatted String
msg = f'{first} [{last}] is a coder'

print(msg)

course = 'Python for Beginners'

# length function
print(len(course))

print(course.upper())
print(course.lower())

print(course.find('P'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.title())

# Find sub String
print('Python' in course)  # true
print('learn-python' in course)  # false

print(course[-3:])  # last 3 characters in the string


