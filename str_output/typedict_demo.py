# TypedDict lets us define the expected structure of a dictionary
from typing import TypedDict


class Person(TypedDict):
    name: str     # Required key "name" with string value
    age: int      # Required key "age" with integer value


p: Person = {"name": "John", "age": 22}  # Create a Person-typed dictionary

# NOTE: ":" is for type hints; "=" is for assignment; p["key"] = value updates dict data


# This is a TYPE ANNOTATION + ASSIGNMENT, not a dict update
# It reassigns p to an int (24), replacing the original dictionary
p: Person['age'] = 24
print("This is the 1st p", p)


# This now fails because p is no longer a dict (it's an int)
# Correct way to update the dictionary value is: p["age"] = 24
p['age'] = 24
print("This is the second p", p)
