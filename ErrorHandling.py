try:
    age = int(input("Age: "))
    risk = 20000 / age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be zero")
