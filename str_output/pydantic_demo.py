from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "Bhavya"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description="cgpa should be between 0 and 10")

new_student : Student = {"age": 21, "email": "jethibhavya@gmail.com", "cgpa": 8.8}
student = Student(**new_student)
student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_dump_json()