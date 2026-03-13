 # Stdents management system.
 # Python is a dynamically typed language, which is there is not much restriction in data type. But in real world scenario this is not ideal.
 # For real world scenario there should be restricted data type, validation and restriction should be there for the incoming data .
 # Type hinting - you must hint what kind of data you want 

def create_student(name, age, college):
    print(name)
    print(age)
    print(college)
    print("Student Created!")

create_student("Sanskriti", 23, "Masai")    

# Type_Hinting - specifying the data type (next terminal)

def create_student(name: str, age: int, college: str):

    if type(name)==str and type(age)==int and type(college)==str:
        print(name)
        print(age)
        print(college)
        print("Student Created!")
    else:
        raise TypeError("Invalid type of input data")
create_student("Sanskriti", 23, "Masai") 

 # Mentioning the if and else function in all the atrributes is very difficult and it might ask you to repeat the code base.
 # This drawback lead to the concept of Pydantic
 # DRY - Don't Repeat Yourself (Try to reuse the code)
 # Pydantic - one of the most powerful library in python that gives you data validation
 # You can give rules at one place and enforce it at multiple places for that kind of data  
 # Step 1- Create an Ideal Model class(Base model class) using Pydantic
 # Base model means any class for which that will have an object that needs to created so that it will store data for e.g. Student

