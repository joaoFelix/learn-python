is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")


def mean(value):
    # or with same condition written differently (type() vs isinstance())
    if type(value) == dict or isinstance(value, dict):
        return sum(value.values()) / len(value)
    else:
        return sum(value) / len(value)


print(mean([1, 2, 3]))
print(mean({"Mary": 8.0, "Sim": 9.0, "Zack": 10.0}))