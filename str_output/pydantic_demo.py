from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "Bhavya"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description="cgpa should be between 0 and 10")

new_student : Student = {"age": 21, "email": "jethibhavya@gmail.com", "cgpa": 8.8}

# **new_student unpacks the below line from dict into keyword arguments and so creates a pydantic model called student.
student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])

# .model_dump_json(), it converts the model to a json string, its useful when sending data to api, saving to files and serializing objects
student_json = student.model_dump_json()