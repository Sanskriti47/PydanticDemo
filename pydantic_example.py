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
