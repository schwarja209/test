def classify_person(name, age):
    """
    Create a function that returns whether a person is a child, teenager, adult, or senior based on their age
    Under 13: "[name] is a child."
    13-19: "[name] is a teenager."
    20-64: "[name] is an adult."
    65+: "[name] is a senior."
    """
    if age < 13:
        print(name, "is a child")
    elif age < 20:
        print(f"{name} is a teenager")
    elif age < 65:
        print(f"{name} is an adult")
    else:
        print(f"{name} is a senior")

# Test cases
classify_person("Alex", 10)
classify_person("Jamie", 15)
classify_person("Taylor", 30)
classify_person("Morgan", 70)

name=input("Please state the name of a person: ")
age=int(input("Please state this person's age: "))

classify_person(name, age)