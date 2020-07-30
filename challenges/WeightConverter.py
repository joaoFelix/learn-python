weight = float(input("Weight: "))
unit = input("(L)bs or (K)g? ").upper()

if unit == "L":
    print(f"You are {weight * 0.45} Kg")
elif unit == "K":
    print(f"You are {weight / 0.45} Lbs")
else:
    print(f"Unknown unit {unit}")