# {} define dictionaries
# Keys are unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) # John Smith

# customer["birthdate"] = Error (birthdate does not exist)
print(customer.get("birthdate")) # None
print(customer.get("birthdate", "Jan 1st 1980")) # Default value
