from pydantic import BaseModel, Field, EmailStr, field_validator

class Student(BaseModel):
    name: str
    age: int = Field(gt=0,le=100)
    college: str 
    email: EmailStr 
    marks: float = Field(default = 10, description = "Please provide the exact marks.")

@field_validator("email")
@classmethod
def email_validator(cls,value):
    domain_name = value.split("@")[-1]
    if domain_name != "gmail.com":
        raise ValueError("Invalid domain")
    return value 

@field_validator('college')
@classmethod
def converting_college_into_lower_case(cls, value):
    return value.lower()

student_info = {'name': 'Sanskriti', 'age': 23, 'email': 'sanskriti@gmail.com', 'college': 'MASAI'}

student = Student(**student_info)
print(student.email)
print(student.college)

# mode = before, means that the value of a particular class to be converted before , by default it is after

#Serialisation and Deserialisation 
# Sometimes the backend can be written in java and frontend in python. java converts to json and then json converts into python.
# This process is called as serialisation and deserialisation. First serialisation happens then packing and unpacking (its internal concept)

