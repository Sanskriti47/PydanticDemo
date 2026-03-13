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

def create_student(name: str, age: int, college: str):

    if type(name)==str and type(age)==int and type(college)==str:
        print(name)
        print(age)
        print(college)
        print("Student Created!")
    else:
        raise TypeError("Invalid type of input data")
create_student("Sanskriti", 23, 10) 