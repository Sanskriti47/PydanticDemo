 # Mentioning the if and else function in all the atrributes is very difficult and it might ask you to repeat the code base.
 # This drawback lead to the concept of Pydantic
 # DRY - Don't Repeat Yourself (Try to reuse the code)
 # Pydantic - one of the most powerful library in python that gives you data validation
 # You can give rules at one place and enforce it at multiple places for that kind of data  
 # Step 1- Create an Ideal Model class(Base model class) using Pydantic
 # Base model means any class for which that will have an object that needs to created so that it will store data for e.g. Student
 # By default all the fields are mandatory in the base model, if you miss any one it will raise ValidationError
 # To make it optional you have to put = and any value for eg. college: str = None

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int = None
    college: str

student_info = {'name': 'Sanskriti', 'age': '20', 'college': 'Masai'}
# Using the student_info dict, create the student object.
# ** - means unpacking, converting any list, bracket to an object
student =  Student(**student_info)
# As we have passed what type of data we require for Student in the class, hence if that kind of data is not provided in the dictionary, pydantic will raise a validation error.

print(student.name)
print(student.age)
print(student.college)

# To make a field optional you can define the value for it in the class provided, eaier method.
# Type Validations in pydantic -Validating the type of the attributes.

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int 
    college: str = None
    marks: float

student_info = {'name': 'Sanskriti', 'age': 23, 'marks': '80.9'}
# Using the student_info dict, create the student object.
# ** - means unpacking, converting any list, bracket to an object
student =  Student(**student_info)
# As we have passed what type of data we require for Student in the class, hence if that kind of data is not provided in the dictionary, pydantic will raise a validation error.

print(student.name)
print(student.age)
print(student.college)
print(student.marks)

# To make sure that the user passes correct value of a data and not in negatives, we do field validation
# Field Validation - Validating the field value 
# Example - greater than or less than, maximum length of any string, email validation 
# gt = greater than, lt = less than, ge = greater than equal, le = less than equal
# To validate you need to import it from the pydantic 

from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field (max_length=10)
    age: int = Field(gt = 0, le = 100)
    college: str = None
    marks: float = Field(default = 0.0, gt = 0, le = 100)

student_info = {'name': 'Sanskriti', 'age': 23 , 'marks': '99.9'}  

student = Student(**student_info)

print(student.name)
print(student.age)
print(student.college)
print(student.marks)

# Making use of Email Validation
# You need to extract the Emailstr from the pydantic to make use of email 

from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name: str
    age: int = Field(gt=0,le=100)
    college: str = 'Masai'
    email: EmailStr
    marks: float

student_info = {'name':'Sanskriti', 'age':23, 'email':'sanskritijain47@gmail.com', 'marks':'99.9'}

student = Student(**student_info)
print(student)

# If you want to take some URL, AnyUrl is used, Httpsurl

from pydantic import BaseModel, Field, EmailStr, AnyUrl, HttpUrl

class Student(BaseModel):
    name: str
    age: int = Field(gt=0,le=100)
    college: str = 'Masai'
    email: EmailStr
    marks: float
    url: HttpUrl

student_info = {'name':'Sanskriti', 'age':23, 'email':'sanskritijain47@gmail.com', 'marks':'99.9', 'url': 'https://pin.it/kk'}

student = Student(**student_info)
print(student.url)

# Making use of default 
class Student(BaseModel):
    name: str
    age: int = Field(gt=0,le=100)
    college: str = 'Masai'
    email: EmailStr
    marks: float = Field(default = 10)

student_info = {'name':'Sanskriti', 'age':23, 'email':'sanskritijain47@gmail.com',}

student = Student(**student_info)
print(student)

# If you mention some random field, and that is not present in the class, it will simply ignore it 
# You can make use of examples and description in the field in order to provide certain example

class Student(BaseModel):
    name: str
    age: int = Field(gt=0,le=100)
    college: str = 'Masai'
    email: EmailStr = Field(description = "The email looks like this-", examples = "ABC@gmail.com")
    marks: float = Field(default = 10, description = "Please provide the exact marks.")

student_info = {'name':'Sanskriti', 'age':23, 'email':'sanskritijain47@gmail.com',}

student = Student(**student_info)
print(student.email)
print(student.marks)

# Suppose if you want a specific email validation, suppose @gmail.com should be the only accepted email 

from pydantic import BaseModel, Field,  EmailStr, field_validator

class Student(BaseModel):
    name: str
    age: int = Field(gt=0,le=100)
    college: str = 'Masai'
    email: EmailStr = Field(description = "The email looks like this-", examples = "ABC@gmail.com")
    marks: float = Field(default = 10, description = "Please provide the exact marks.")

 # This field validator makes sure that the email value belongs to @gmail.com    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # in order to get the domain name, we make use of split function
        domain_name = value.split('@')[-1]
        if domain_name == '@gmail.com' :
            print("Valid Domain name")

        else:
            raise ValueError("Invalid Domain name")
        
        return value

student_info = {'name':'Sanskriti', 'age':23, 'email':'sanskritijain47@gmail.com'}

student = Student(**student_info)
#print(student.email)

#After validating any daya, if you want to convert it into any form. For r.g. in marks, want to calculate total marks and percentage, field validators can be used.

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
    if domain_name != "masai.com":
        raise ValueError("Invalid domain")
    return value 

@field_validator('college')
@classmethod
def converting_college_into_lower_case(cls, value):
    return value.lower()

student_info = {'name': 'Sanskriti', 'age': 23, 'email': 'sanskriti@masai.com', 'college': 'MASAI'}

student = Student(**student_info)
print(student.email)
print(student.college)
