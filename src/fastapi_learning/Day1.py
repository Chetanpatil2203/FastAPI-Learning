# Task 1 — Easy: Create GET endpoints
# Create these two endpoints:

# 1. GET /courses


from fastapi import FastAPI

app = FastAPI()

# @app.get("/courses")
# def courses():
#     return[
#         "python",
#         "FastAPI",
#         "PostgreSQL",
#         "AI Engineering"
#     ]






# Return:
# [    "Python",    "FastAPI",    "PostgreSQL",    "AI Engineering"]



# 2. GET /students/{student_id}
# - Accept an integer student_id.
# - Return the student ID in JSON.
# Example: /students/25

# @app.get("/students/{student_id}")
# def student_id(student_id:int):
#     return{
#         "student_id" : student_id
#     }
# Expected response:
# {
#     "student_id": 25
# }


# Task 2 — Medium: Query parameters
# Create:

# GET /students?limit=10

# Requirements:
# - Accept a limit query parameter.
# - Default value should be 10.
# - Return the limit in JSON.
# Example response:
# {
#     "limit": 10
# }
# @app.get("/students")
# def students(limit:int=10):
#     return{
#         "limit":limit
#     }



# File: day-01/main.py

# Create this endpoint:

# GET /courses

# Requirements:
# 1. Accept a query parameter called category.
# 2. Default value should be "Python".
# 3. Return the category in JSON.

# @app.get("/courses")
# def courses(category:str = "python"):
#     return{
#         "category":category
#     }


# Task 1 — Easy: Student details
# Create:

# GET /students/{student_id}

# Requirements:
# - Accept an integer student_id.
# - Return the student ID.
# Expected response for /students/25:

# @app.get("/students/{student_id}")
# def student_details(student_id:int):
#     return{
#         "student_id":student_id
#     }

# Next: Task 2 — Course details
# FASTAPI LEARNING
# Repository: fastapi-learning

# Create:

# GET /courses/{course_id}

# Requirements:
# - Accept an integer course_id.
# - Return the course ID and message.
# Expected response for /courses/5:

# @app.get("/courses/{course_id}")
# def course_details(course_id:int):
#     return{
#         "message": "successful return",
#         "course_id":course_id
#     }


# ask 3 — Medium: Product details
# FASTAPI LEARNING
# Create:

# GET /products/{product_name}

# Requirements:
# 1. Accept a string product_name.
# 2. Return the product name.
# Expected response for /products/laptop:

@app.get("/products/{product_name}")
def product_details(product_name:str):
    return{
        "product_name" : product_name
    }