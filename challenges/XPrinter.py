numbers = [2, 2, 2, 2, 5]

# Done as if print('x' * x_count) wasn't possible
for x_count in numbers:
    x_str = ''
    for idx in range(x_count):
        x_str += 'x'
    print(x_str)
