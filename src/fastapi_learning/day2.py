# # Task 1: Create a Pydantic model for a Course.

# # Requirements:
# # 1. Import BaseModel.
# # 2. Create a class named Course.
# # 3. Add these fields:
# #    - course_name: string
# #    - duration: integer
# #    - price: float


from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict,Field
from typing import Annotated

app = FastAPI()

# class Course(BaseModel):
#     course_name:str
#     duration:int
#     price:float


# course= Course(
#     course_name="Python Backend",
#     duration="60",
#     price=4999.0
# )

# print(course)
# print(course.model_dump())


# #Strict Mode
# class Product(BaseModel):
#     model_config=ConfigDict(strict=True)
#     name: str
#     price: float
#     quantity: int

# product = Product(
#     name="Lenovo",
#     price = "24",
#     quantity = 10

# )    

# print(product)


# 6. Your exercise
# FASTAPI LEARNING
# Continue in src/fastapi_learning/Day2.py.

# Create this model yourself:

# Employee
# - name: required string.
# - age: integer with default value 22.
# - email: optional string with default None.
# - salary: float with default value 15000.0.
# Then create two Employee objects:
# 1. One with all four fields.
# 2. One with only name.
# Print both objects.


# class Employee(BaseModel):
#     name:str
#     age:int=22
#     email:str|None
#     salary:float=15000

# details = Employee(
#      name = "chetan",
#      age = 24,
#      email = "chetanpatil0322@gmail.com",
#      salary = 200000

#  )  

# print(details) 

# e1 = Employee(name="vikas")
# print(e1)

#field function

# Create this model yourself:
# class Product(BaseModel):    # Apply the required Field() rules    ...



# Requirements:
# 1. name: string, minimum 3 and maximum 30 characters.
# 2. price: float, greater than 0.
# 3. quantity: integer, greater than or equal to 1.
# 4. description: optional string, maximum 100 characters.

class Product(BaseModel):
    name:str = Field(min_length=3,max_length=30 )
    price:float = Field(gt=0)
    quantity:int = Field(ge=1)
    description:str|None=None; Field(max_length=100)

p1 =Product(
    name="Lenovo Laptop",
    price=50000,
    quantity=2,
    description="A" * 101
) 

print(p1)


#Annotated
# Create an Employee model using Annotated.

# Requirements:
# Field	Validation
# name	String, minimum 3 characters
# age	Integer, 18–60
# salary	Float, greater than 0

# Use Annotated and Field() for all three fields.

class Employee(BaseModel):
    name:Annotated[str,Field(min_length=3)]
    age:Annotated[int,Field(ge=18 , le=60)]
    salary:Annotated[float,Field(gt = 0)]


e1 = Employee(
    name = "chetan",
    age= 24,
    salary = 24444
)    

