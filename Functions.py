# Positional arguments
def greet_user_pos(name):
    print(f"Hello there, {name}!")

# Keyword arguments
def greet_user_key(first_name, last_name):
    print(f"Hello there, {first_name} {last_name}!")


greet_user_pos("John")
greet_user_key(last_name="Felix", first_name="John")

def square(number):
    return number ** 2


print(square(3))  # 9
