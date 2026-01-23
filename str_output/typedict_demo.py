# TypedDict lets us define the structure of a dictionary
from typing import TypedDict

class Person(TypedDict): 
    name: str 
    age: int

p : Person = {"name":"John", "age": 22}

# Running both the codes will cause the 2nd code to throw an error as the 1st one converts dict to int by data annotation and 2nd tries to do an item assign which throws an error. If u comment the 1st code and run the 2nd it successfully updates the age in the dict and returns it.
p: Person['age'] = 24
print("This is the 1st p", p)
p['age'] = 24
print("This is the second p", p)