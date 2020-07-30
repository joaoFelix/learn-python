has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan (AND)")

if has_high_income or has_good_credit:
    print("Eligible for loan (OR)")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan (NOT)")

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("Int's not a hot day")

